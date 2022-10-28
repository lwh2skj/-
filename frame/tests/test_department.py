from frame.apis.department import Department


class TestDepartment:
    def setup_class(self):
        # 实例化部门类
        self.department = Department()
        # 准备测试数据
        self.department_id = 32
        self.create_data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "id": self.department_id
        }

        self.update_data = {
            "name": "2skj_update",
            "id": self.department_id
        }

    def test_department(self):
        """
        创建部门 -> 更新部门 -> 删除部门
        :return:
        """
        self.department.create(self.create_data)
        # 断言是否创建成功
        depart_list = self.department.get().get("department_id")
        department_list = [data.get("id") for data in depart_list]
        # print(depart_list)
        assert self.department_id in department_list
        print(department_list)

        # # 修改部门信息
        self.department.update(self.update_data)
        # # 断言是否修改成功
        depart_list = self.department.get().get("department_id")
        department_list = [data.get("id") for data in depart_list]
        assert self.department_id in department_list
        # 删除部门
        self.department.delete(self.department_id)
        # # # 断言是否删除成功
        depart_list = self.department.get().get("department_id")
        department_list = [data.get("id") for data in depart_list]
        assert self.department_id not in department_list
