import requests

from intermediate.apis.base_api import BaseApi


class Goods(BaseApi):

    def create(self, goods_data):
        url = "admin/goods/create"
        # 问题token是手动复制进去的一旦发生变化还需要再次修改
        # 解决方案：token需要自动完成获取并且赋值
        # r = requests.post(url, json=goods_data, headers={"X-Litemall-Admin-Token": self.token})
        r = self.send("post", url, json=goods_data, headers={"username": "admin123"})
        return r

    def list(self, goods_name, order="desc", sort="add_time"):
        # 自己编写的接口的方法，应该和接口本身的逻辑相关
        good_list_url = "admin/goods/list"
        good_data = {
            "name": goods_name,
            "order": order,
            "sort": sort
        }

        r = self.send("get", good_list_url,
                      params=good_data,
                      # headers={"X-Litemall-Admin-Token": self.token}
                      )
        return r

    def detail(self, goods_id):
        goods_detail_url = "admin/goods/detail"
        r = self.send("get", goods_detail_url,
                      params={"id": goods_id}
                      )
        return r
        # product_id = r.json()["data"]["products"][0]["id"]

    def delete(self, goods_id):
        url = "wx/cart/delete"
        r = self.send("post", url, json={"id": goods_id})
        return r