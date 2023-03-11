from tools import httpTools
from init import conf

import json


def feishu_hook(title, text, status, text_url_title, text_url):
    """
    make request to feishu's webhook
    """

    if status == "future":
        status = "未开始"
    elif status == "active":
        status = "进行中"
    elif status == "complete":
        status = "已完成"
    else:
        status = "未知状态"

    payload = {
        "msg_type": "interactive",
        "card": {
            "elements": [{
                    "tag": "div",
                    "text": {
                            "content": f'**状态:{status}**\r\n'
                                       f'{text}',
                            "tag": "lark_md"
                    }
            }, {
                    "actions": [{
                            "tag": "button",
                            "text": {
                                    "content": text_url_title + " :玫瑰:",
                                    "tag": "lark_md"
                            },
                            "url": text_url,
                            "type": "default",
                            "value": {}
                    }],
                    "tag": "action"
            }],
            "header": {
                    "title": {
                            "content": f'[{title}]版本动态',
                            "tag": "plain_text"
                    }
            }
        }
    }
    r = httpTools.post(conf.feishu_version_bot_url, data=json.dumps(payload))
    if r.json().get('StatusCode') == 0:
        return 200
    return 500
