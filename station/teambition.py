import datetime
import json

import jwt

from tools import httpTools, fileTools
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

    # 根据获取的结果，存储到临时文件
    # save_sprint_to_file(json.loads(response.text))

    return response


"""
初始化迭代列表
"""
os = fileTools.FileTools(conf.sprint_file_path)
if not os.file_exists():
    # 如果不存在，则是第一次加载，需要创建json文件
    jdata = get_sprint_list(conf.project_id)
    print(f'===>{jdata.text}')
    os.write_file(jdata)
else:
    # 如果存在，则需要加载数据到sprintList
    sprint_list = os.read_file()

# os.close_file()


if __name__ == '__main__':
    # res = get_sprint_list("6194786457129d43a36fd201")
    # print(f'===>{res.text}')
    pass
