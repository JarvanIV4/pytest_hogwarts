# -*- coding:utf-8 -*-
from common.interface.HttpAPI import HttpAPI
from config.interface import queryMobileConfig as qmc


class queryInfo(HttpAPI):

    def __init__(self, user):
        super().__init__()
        self.get_loginCookie(user)

    def login_sys_api(self, user="用户1", login_url="ST"):
        if login_url == "ST":
            login_resp = self.send(qmc.api_data, qmc.setting)   # 发送登录接口请求
        elif login_url == "UAT":
            login_resp = self.send(qmc.api_data, qmc.setting)  # 发送登录接口请求

    def get_loginCookie(self, user):
        self.login_sys_api(user)

