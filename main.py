import time
import json
import json_tools

from station import teambition, feishu
from init import conf
from station.teambition import get_sprint_list
from tools import fileTools

if __name__ == '__main__':
    # 初始化数据库
    teambition.init_sprint_data()

    # 开始定时任务循环
    while True:
        # 循环调用diff_script_list方法，对比数据库中的迭代列表和最新的迭代列表
        jsonlist = teambition.diff_script_list()
        # 如果有更新，则发送飞书消息
        if jsonlist:

            for item in jsonlist:
                res = feishu.feishu_hook(item.name, item.description, item.status, "查看详情(开发中)", "")
                if res == 200:
                    print("==>发送成功!")
                else:
                    print("==>发送失败!")
        else:
            print("==>无更新")
        time.sleep(10)
