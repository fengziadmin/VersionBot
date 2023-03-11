"""
from flask import Flask

app = Flask(__name__)




如果需要teambition需要通过webhook转调用feishu的webhook，可以参考下面的代码


@app.route('/hook', methods=['POST'])
def web_hook():
    
    transfer station of teambition's webhook to feishu's webhook

    # resolve teambition's request, maybe we need some authentication
    signature = request.headers.get('X-Signature', '')

    response = request.json

    type = response['event']
    task_state_map = {'task.create': '创建任务', 'task.update': '更新任务', 'task.remove': '删除任务'}

    if type not in list(task_state_map.keys()):
        return jsonify({"code": 200, "status": 'success'})

    task_state = task_state_map.get(type)

    task_id = response['db']['task']['taskId']
    task_url = 'https://www.teambition.com/task/{}'.format(task_id)

    task_content = response['db']['task']['content']
"""