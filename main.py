from flask import Flask, request, jsonify

import requests
import json

app = Flask(__name__)


@app.route('/hook', methods=['POST'])
def web_hook():
    """
    transfer station of teambition's webhook to feishu's webhook

    # resolve teambition's request, maybe we need some authentication
    signature = request.headers.get('X-Signature', '')

    response = request.json

    type = response['event']
    task_state_map = {'task.create': '创建任务', 'task.update': '更新任务', 'task.remove': '删除任务'}

    if type not in list(task_state_map.keys()):
        return jsonify({"code": 200, "status": 'success'})

    task_state = task_state_map.get(type)

    task_id = response['data']['task']['taskId']
    task_url = 'https://www.teambition.com/task/{}'.format(task_id)

    task_content = response['data']['task']['content']
    """
    # make request to feishu's webhook
    payload = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "版本人机器人提醒您",
                    "content": [
                        [
                            {
                                "tag": "text",
                                "text": "{}({}):"
                            },
                            {
                                "tag": "a",
                                "text": 'task_url',
                                "href": 'task_url'
                            }
                        ]
                    ]
                }
            }
        }
    }
    web_hook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/51620427-8bf8-48be-9b88-bb8b6ce9ada7'
    r = requests.post(web_hook_url, data=json.dumps(payload))
    if r.json().get('StatusCode') == 0:
        return jsonify({"code": 200, "status": 'success'})
    return jsonify({"code": 203, "status": 'error'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)