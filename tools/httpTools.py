import requests

"""
封装的公共服务类，包含常用的HTTP请求方法
"""


def get(path, headers=None, params=None):
    """
    发送GET请求
    :param path: 请求路径，字符串类型
    :param headers: 请求头部信息，字典类型
    :param params: 请求参数，字典类型
    :return: 返回响应对象，可以通过response.json()方法获取JSON格式的响应内容
    """
    url = path
    response = requests.get(url, headers=headers, params=params)
    return response


def post(path, headers=None, data=None, json=None):
    """
    发送POST请求
    :param path: 请求路径，字符串类型
    :param headers: 请求头部信息，字典类型
    :param data: 请求数据，字典类型
    :param json: 请求数据，JSON格式的字符串或字典类型
    :return: 返回响应对象，可以通过response.json()方法获取JSON格式的响应内容
    """
    url = path
    response = requests.post(url, headers=headers, data=data, json=json)
    return response


def put(path, headers=None, data=None, json=None):
    """
    发送PUT请求
    :param path: 请求路径，字符串类型
    :param headers: 请求头部信息，字典类型
    :param data: 请求数据，字典类型
    :param json: 请求数据，JSON格式的字符串或字典类型
    :return: 返回响应对象，可以通过response.json()方法获取JSON格式的响应内容
    """
    url = path
    response = requests.put(url, headers=headers, data=data, json=json)
    return response


def delete(path, headers=None, params=None):
    """
    发送DELETE请求
    :param path: 请求路径，字符串类型
    :param headers: 请求头部信息，字典类型
    :param params: 请求参数，字典类型
    :return: 返回响应对象，可以通过response.json()方法获取JSON格式的响应内容
    """
    url = path
    response = requests.delete(url, headers=headers, params=params)
    return response
