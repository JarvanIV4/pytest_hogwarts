import logging

class IndexOps():

    def switch_to_popup(self):
        """切换至菜单页面的弹窗iframe"""
        # logger.info(self.deriver.find_element_tag_name('iframe'))
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name('iframe')[-1])
        # logger.info(self.deriver.find_element_tag_name('iframe'))

    def switch_back_to_iframe(self):
        """从弹窗切换至弹窗前的iframe"""
        # logger.info(self.deriver.find_element_tag_name('iframe'))
        self.driver.switch_to.default_content()
        self.driver.find_elements_by_tag_name('iframe')
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name('iframe')[-1])
        # logger.info(self.deriver.find_element_tag_name('iframe'))

    def query_sql(self, sqlstr, return_type="tuple"):
        try:
            self.cursor = self.database.cursor()
            cursor = self.cursor.execute(sqlstr)  # 执行查询
            if return_type == 'tuple':
                result = self.cursor.fetchall()
                return result
            if return_type == 'dict':
                columns = [i[0] for i in cursor.description]
                result = [dict(zip(columns, row) for row in cursor)]
                return result
        except:
            self.database.rollback()

