import os


class FileControl:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.revert_src = []
        self.revert_dst = []

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

    def rename(self, address: str, iteration: bool, file_list: list[str],
               name: str, no: str, suffixif: bool, suffix: str) -> bool:
        # 清空上一次操作
        self.revert_src.clear()
        self.revert_dst.clear()
        # 序号不为空
        if no != '':
            digit = len(no)
            start = int(no)
            try:
                for file in file_list:
                    # 分割文件名和拓展名
                    name_without_ext, ext = os.path.splitext(file)
                    if iteration is False:
                        # 文件新名称若为空则不修改
                        new_name = name if name != '' else name_without_ext
                        if suffixif is False:
                            new_name_ext = new_name + str(start).zfill(
                                digit) + ext
                        else:
                            new_name_ext = new_name + str(start).zfill(
                                digit) + suffix
                        os.rename(os.path.join(address, file),
                                  os.path.join(address, new_name_ext))
                        # 保存上一次操作，供撤销使用
                        self.revert_src.append(os.path.join(address, file))
                        self.revert_dst.append(
                            os.path.join(address, new_name_ext))
                    else:
                        # 分割相对路径和文件名
                        relpath, name_without_relpath = os.path.split(
                            name_without_ext)
                        new_name = name if name != '' else name_without_relpath
                        if suffixif is False:
                            new_name_ext = new_name + str(start).zfill(
                                digit) + ext
                        else:
                            new_name_ext = new_name + str(start).zfill(
                                digit) + suffix
                        os.rename(os.path.join(address, file),
                                  os.path.join(address, relpath, new_name_ext))
                        # 保存上一次操作，供撤销使用
                        self.revert_src.append(os.path.join(address, file))
                        self.revert_dst.append(
                            os.path.join(address, relpath, new_name_ext))
                    start += 1
            except OSError:
                return False
        # 不添加序号
        else:
            # 文件新名称若不为空则错误
            if name != '':
                return False
            try:
                for file in file_list:
                    # 分割文件名和拓展名
                    name_without_ext, ext = os.path.splitext(file)
                    if iteration is False:
                        if suffixif is False:
                            new_name_ext = name_without_ext + ext
                        else:
                            new_name_ext = name_without_ext + suffix
                        os.rename(os.path.join(address, file),
                                  os.path.join(address, new_name_ext))
                        # 保存上一次操作，供撤销使用
                        self.revert_src.append(os.path.join(address, file))
                        self.revert_dst.append(
                            os.path.join(address, new_name_ext))
                    else:
                        # 分割相对路径和文件名
                        relpath, name_without_relpath = os.path.split(
                            name_without_ext)
                        if suffixif is False:
                            new_name_ext = name_without_relpath + ext
                        else:
                            new_name_ext = name_without_relpath + suffix
                        os.rename(os.path.join(address, file),
                                  os.path.join(address, relpath, new_name_ext))
                        # 保存上一次操作，供撤销使用
                        self.revert_src.append(os.path.join(address, file))
                        self.revert_dst.append(
                            os.path.join(address, relpath, new_name_ext))
            except OSError:
                return False
        return True

    def revert(self) -> bool:
        self.revert_src.reverse()
        self.revert_dst.reverse()
        revert_list = list(zip(self.revert_src, self.revert_dst))
        for src, dst in revert_list:
            os.rename(dst, src)
        self.revert_src.clear()
        self.revert_dst.clear()
