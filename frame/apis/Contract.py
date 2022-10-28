import os.path

from frame.apis.wework import Wework
from frame.utils.file_utils import FileUtils


class Contract(Wework):

    def __init__(self):
        """
        获取通讯录管理的token
        """
        # 读取配置文件中的key
        # config_data = FileUtils.get_yaml_data(os.sep.join([FileUtils.get_frame_dir(), "datas/config.yaml"]))
        corpid = self.config_data.get("corpid").get("2skj")
        secret = self.config_data.get("secret").get("contract")
        self.access_token = self.get_access_token(corpid, secret)
