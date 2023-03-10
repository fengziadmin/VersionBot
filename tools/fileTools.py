import os


class FileTools:
    def __init__(self, filename, mode=os.O_RDWR | os.O_CREAT):
        self.filename = filename  # 文件名
        self.mode = mode  # 打开文件的模式
        self.file = None

    def file_exists(self):
        return os.path.exists(self.filename)

    def open_file(self):
        try:
            self.file = open(self.filename, self.mode)  # 打开文件
        except IOError as e:
            print("Error: {}".format(e))

    def read_file(self):
        if self.file is not None:
            try:
                data = self.file.read()  # 读取文件内容
                return data
            except IOError as e:
                print("Error: {}".format(e))

    def write_file(self, data):
        #if self.file is not None:
        try:
            self.file.write(data)  # 写入数据到文件
        except IOError as e:
            print("Error: {}".format(e))

    def append_file(self, data):
        if self.file is not None:
            try:
                self.file.write(data)  # 追加数据到文件
            except IOError as e:
                print("Error: {}".format(e))

    def close_file(self):
        if self.file is not None:
            self.file.close()  # 关闭文件

    def delete_file(self):
        try:
            os.remove(self.filename)  # 删除文件
        except OSError as e:
            print("Error: {}".format(e))
