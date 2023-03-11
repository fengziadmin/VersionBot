import os


def file_exists(file_path):
    """
    判断文件是否存在
    param filePath: 文件路径
    return bool  : 是否存在
    """
    return os.path.exists(file_path)

def get_File_List(dir, file_list=None):
    """
    遍历一个目录,输出所有文件名
    param dir: 待遍历的文件夹
    param filrList : 保存文件名的列表
    return fileList: 文件名列表
    """
    if file_list is None:
        file_list = []
    if os.path.isfile(dir):
        file_list.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
            # continue
            new_dir = os.path.join(dir, s)
            get_File_List(new_dir, file_list)
    return file_list


def readStrFromFile(file_path=None):
    """
    从文件中读取字符串str
    param filePath: 文件路径
    return string : 文本字符串
    """
    with open(file_path, "rb") as f:
        string = f.read()
    return string


def readLinesFromFile(file_path):
    """
    从文件中读取字符串列表list
    param filePath: 文件路径
    return lines  : 文本字符串列表
    """
    with open(file_path, "r") as f:
        lines = f.readlines()
    return lines


def writeStrToFile(file_path, string):
    """
    将字符串写入文件中
    param filePath: 文件路径
    param string  : 字符串str
    """
    with open(file_path, "w") as f:
        f.write(string)


def appendStrToFile(file_path, string):
    """
    将字符串追加写入文件中
    param filePath: 文件路径
    param string  : 字符串str
    """
    with open(file_path, "a", encoding='utf-8') as f:
        f.write(string)


def dumpToFile(file_path, content):
    """
    将数据类型序列化存入本地文件
    param filePath: 文件路径
    param content : 待保存的内容(list, dict, tuple, ...)
    """
    import pickle
    with open(file_path, "w") as f:
        pickle.dump(content, f)


def loadFromFile(file_path):
    """
    从本地文件中加载序列化的内容
    param filePath: 文件路径
    return content: 序列化保存的内容(e.g. list, dict, tuple, ...)
    """
    import pickle
    with open(file_path) as f:
        content = pickle.load(f)
    return content
