import datetime
import json
import jwt

from db.db import *
from tools import httpTools
from init import conf

# 声明迭代列表
global sprint_list


def get_token(now):
    """
    获取teambition 的临时 token
    """
    header = {
    }
    payload = {
        '_appId': conf.app_id,
        'iat': now,
        'exp': now + datetime.timedelta(seconds=3600)
    }
    token = jwt.encode(payload, conf.app_secret, algorithm='HS256', headers=header)

    return token


def get_sprint_list(project_id):
    """
    通过项目ID获取迭代列表
    :param project_id:
    :return:
    """
    token = get_token(datetime.datetime.now())
    path = conf.teambition_sprint_url.format(project_id)
    headers = {
        'Authorization': token,
        'X-Tenant-Id': conf.x_tenant_id,
        'X-Tenant-Type': conf.x_tenant_type
    }
    response = httpTools.get(path, headers=headers)
    return response


def init_sprint_data():
    """
    初始化迭代数据库
    """
    # 初始化数据库
    # 如果表不存在，则创建表
    if not Sprint.table_exists():
        # 开始初始化数据库
        print('==>初始化数据库')
        # 创建迭代表
        Sprint.create_table()
        # 获取迭代列表
        response = get_sprint_list(conf.project_id)
        slist = json.loads(response.text)['result']

        # 写入本地db文件
        for sprint in slist:
            obj = Sprint()
            obj.sprint_id = sprint['id']
            obj.name = sprint['name']
            obj.projectId = sprint['projectId']
            obj.description = sprint['description']
            obj.status = sprint['status']
            obj.save()


def diff_script_list():
    """对比数据库中的迭代列表和最新的迭代列表"""
    # 获取最新的迭代列表
    slist = json.loads(get_sprint_list(conf.project_id).text)['result']

    return_list = []
    # 遍历最新的迭代列表
    for item in slist:
        new_obj = Sprint()
        new_obj.sprint_id = item['id']
        new_obj.name = item['name']
        new_obj.projectId = item['projectId']
        new_obj.description = item['description']
        new_obj.status = item['status']
        # 如果数据库中不存在，则插入
        old_obj = Sprint.get_or_none(Sprint.sprint_id == new_obj.sprint_id)
        # 如果数据库中存在，再对比其他字段是否有变化，则更新并且返回item到return_list
        if old_obj:
            if old_obj.name != new_obj.name or old_obj.description != new_obj.description or old_obj.status != new_obj.status:
                print(f'==>更新迭代：{new_obj.name}')
                old_obj.name = new_obj.name
                old_obj.description = new_obj.description
                old_obj.status = new_obj.status
                old_obj.save()
                return_list.append(new_obj)
        else:
            print(f'==>新增迭代：{new_obj.name}')
            new_obj.save()
            return_list.append(new_obj)
    return return_list
