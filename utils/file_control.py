import os


class FileControl:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        pass

    def getfiles(self, path: str, iteration: bool = False):
        cPath = path
        # 如果目录名字为中文 需要转码处理
        uPath = str(cPath)
        if iteration is False:
            return filter(os.path.isfile, os.listdir(uPath))
        else:
            files_list = []
            for root, _, files in os.walk(uPath):
                # root 表示当前正在访问的文件夹路径
                # dirs 表示该文件夹下的子目录名list
                # files 表示该文件夹下的文件list
                # 遍历文件
                for f in files:
                    rel_path = os.path.relpath(root, uPath)
                    files_list.append(os.path.join(rel_path, f))
            return files_list
