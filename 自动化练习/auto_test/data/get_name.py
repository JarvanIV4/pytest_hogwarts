#产生随机数据
from random import Random
import time

class get_data():

    def get_ran_name(self):
        #获取随机名称
        ran = Random()
        base = "abcdefghijklmnopqrstuvwxyz1234567890"
        name = ""
        for j in range(ran.randint(5,10)):
            m = ran.randrange(len(base)-1)
            name = name + base[m]
        return name

    def ran_name(self):
        """产生随机人名"""
        last_name = "赵李张王刘"
        ran = Random()
        m = ran.randrange(len(last_name)-1)
        name = last_name[m]
        first_name = "科成功和兴伟"
        for j in range(ran.randint(2)):
            m = ran.randrange(len(first_name)-1)
            name = name + first_name[m]
        return name

a = get_data()
print(a.ran_name())





