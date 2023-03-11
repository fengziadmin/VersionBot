from configparser import ConfigParser

import os

# feishu
global feishu_version_bot_url

# teambition
global app_id
global app_secret
global teambition_sprint_url
global x_tenant_id
global x_tenant_type
global project_id
global sprint_path
global sprint_db_file_path

# 读取配置文件
config = ConfigParser()
config.read("E:\Github\VersionBot\config.ini", encoding='utf-8')

feishu_version_bot_url = config.get('feishu', 'version_bot_url')
app_id = config.get('teambition', 'app_id')
app_secret = config.get('teambition', 'app_secret')
teambition_sprint_url = config.get('teambition', 'sprint_url')
x_tenant_id = config.get('teambition', 'x_tenant_id')
x_tenant_type = config.get('teambition', 'x_tenant_type')
project_id = config.get('teambition', 'project_id')
sprint_db_file_path = config.get('sqlite3', 'sprint_db_file_path')
print("==>配置文件加载完毕...")
