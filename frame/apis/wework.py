
from frame.apis.base_api import BaseApi


class Wework(BaseApi):

    # def __init__(self, corpid, secret):
        # self.access_token = self.get_access_token(corpid, secret)

    def get_access_token(self, corpid, secret):
        """
        获取access_token的值
        return:token
        """
        # corpid = "ww2ce49636d5419ceb"
        # secret = "pF4hlMG6tXwZpXqGoZ1O9Is1eKndszMwR_mdBYOKh-s"
        # 定义url
        token_url = f"/gettoken?corpid={corpid}&corpsecret={secret}"
        # 定义入参查询参数
        data = {
            "corpid": corpid,
            "corpsecret": secret
        }
        # 发起get请求
        token_r = self.send(method="get", url=token_url, params=data)
        # 打印json
        print(token_r.json())
        # 提取token的值
        return token_r.json().get("access_token")

