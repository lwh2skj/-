from frame.apis.Contract import Contract
from frame.apis.wework import Wework
"""
描述部门的管理只关注业务，不需要断言等等
"""


class Department(Contract):
    """
    部门管理接口
    需要继承Wework，此时就能获取Wework中的access_token
    """
    def create(self, data):
        """
        创建部门
        :@data:创建部门的数据体
        :return:
        """
        create_url = '/department/create'
        params = {"access_token": self.access_token}
        r = self.send(method="POST", url=create_url, params=params, json=data)
        return r.json()

    def update(self, data):
        """
        更新部门
        :return:
        """
        update_url = "/department/update"
        params = {"access_token": self.access_token}
        r = self.send(method="post", url=update_url, params=params, json=data)
        return r.json()

    def get(self):
        """
        获取部门
        :return:
        """
        get_url = "/department/simplelist"
        params = {"access_token": self.access_token}
        r = self.send(method="get", url=get_url, params=params)
        return r.json()


    def delete(self, depart_id):
        """
        删除部门
        :return:
        """
        delete_url = "/department/delete"
        params = {"access_token": self.access_token, "id": depart_id}
        r = self.send(method="get", url=delete_url, params=params)
        return r.json()