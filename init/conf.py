from configparser import ConfigParser

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

# 读取配置文件
config = ConfigParser()
config.read('/Users/a123123/Desktop/pro-doc/git-ware/VersionBot/config.ini')
feishu_version_bot_url = config.get('feishu', 'version_bot_url')
app_id = config.get('teambition', 'app_id')
app_secret = config.get('teambition', 'app_secret')
teambition_sprint_url = config.get('teambition', 'sprint_url')
x_tenant_id = config.get('teambition', 'x_tenant_id')
x_tenant_type = config.get('teambition', 'x_tenant_type')
project_id = config.get('teambition', 'project_id')
sprint_file_path = config.get('sysconfig', 'sprint_file_path')
print("==>配置文件加载完毕...")
