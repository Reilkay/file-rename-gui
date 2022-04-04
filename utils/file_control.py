import os


class FileControl:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        pass

    def getfiles(self, path: str, iteration: bool = False) -> list:
        cPath = path
        # 如果目录名字为中文 需要转码处理
        uPath = str(cPath)

        # 使用绝对路径判断是否为文件
        def __isfile(rel_path) -> bool:
            return os.path.isfile(os.path.join(uPath, rel_path))

        if iteration is False:
            return filter(__isfile, os.listdir(uPath))
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

    def getpath(self, start_from: str, start_path: str) -> str:
        if (start_from == 'custom') and (os.path.isdir(start_path)) and (
                start_path != ''):
            return start_path
        elif start_from == 'cwd':
            return os.getcwd()
        else:
            return os.path.expanduser('~')
