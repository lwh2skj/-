import os.path

import yaml



class FileUtils:
    @classmethod
    def get_yaml_data(cls, file_path):
        """
        封装yaml的读取方法
        :file_path: yaml的路径
        :return: 字典格式的数据
        """
        with open(file_path, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def get_frame_dir(cls):
        a_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.dirname(a_path)

if __name__ == '__main__':
    print(f"打印路径{FileUtils.get_frame_dir()}")