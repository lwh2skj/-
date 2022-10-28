import os
import requests
from frame.utils.file_utils import FileUtils
from frame.utils.log_utils import logger


class BaseApi:
    config_data = FileUtils.get_yaml_data(os.sep.join([FileUtils.get_frame_dir(), "datas/config.yaml"]))
    test_env = os.environ.get("test_env")
    BaseURL = config_data.get("wework_env").get("prod")

    def send(self, method, url, **kwargs):
        """
        对request进行二次封装
        :param method:
        :param url:
        :param kwargs:
        :return:
        """
        url = self.BaseURL + url
        logger.info(f"发起接口调用使用的method为：{method}")
        logger.info(f"发起接口调用使用的url为：{url}")
        logger.info(f"发起接口调用使用的params为：{kwargs.get('params')}")
        logger.info(f"发起接口调用使用的data为：{kwargs.get('data')}")
        logger.info(f"发起接口调用使用的json为：{kwargs.get('json')}")
        res = requests.request(method, url, **kwargs)
        logger.info(f"调用接口返回的json为：{res.json()}")

        return res