# VersionBot
 将Teambition的迭代内容同步到飞书自定义机器人
 
## 环境要求
推荐python >=3.9


## 初始化venv环境
```
python -m venv vnev
```

## 依赖的安装
```
pip install - r requirements.txt
```

## 关于db的说明
目前只使用了本地化的sqlite3


## 关于config.ini的说明

```
[feishu]
#版本消息机器人hook地址
version_bot_url = https://open.feishu.cn/open-apis/bot/v2/hook/{这里填写飞书机器id}

[teambition]
app_id = {这里填写teambition的app_id}
app_secret = {这里填写teambition的app_secret}
#组织ID
x_tenant_id = {这里填写teambition的组织ID}
#组织类型
x_tenant_type = organization
#获取所有迭代信息的接口
sprint_url = https://open.teambition.com/api/v3/project/{}/sprint/search
#项目列表  项目ID:6194786457129d43a36fd201 项目名：产品开发
project_id = {这里填写teambition的项目ID,多个项目用逗号隔开}

[sqlite3]
#数据库文件路径
sprint_db_file_path = ../ver_bot.db
```
