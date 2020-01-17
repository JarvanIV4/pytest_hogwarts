# -*- coding:utf-8 -*-
from common.interface.HttpAPI import HttpAPI
from config.interface import query_mobile_conf as qmc
from common.database.DatabaseTool import DatabaseTool
from common.log.Log import Log
from config.Config import PathConfig
import re


class InterfaceOps(HttpAPI, DatabaseTool):

    def __init__(self):
        super().__init__()
        self.log = Log(PathConfig.log_path)

    def login_sys_api(self, user="用户1", login_url="ST"):
        if login_url == "ST":
            login_resp = self.send(qmc.api_data, qmc.setting)   # 发送登录接口请求
        elif login_url == "UAT":
            login_resp = self.send(qmc.api_data, qmc.setting)  # 发送登录接口请求

    def get_loginCookie(self, user):
        login_resp =self.login_sys_api(user)
        cookie = login_resp.header["Set-Cookie"]
        JSESSIONID = (re.findall("JSESSIONID=(.*); Path", cookie))[0]
        cs_session_cookie = (re.findall("cs_session_cookie=(.*); path", cookie))[0]
        cookie = "JSESSIONID=" + JSESSIONID + ";" + "cs_session_cookie=" + cs_session_cookie + ";" + \
                 "BIGipServerPL_CSST_80=RD501O000000000FFFF370F36CCO80; loginType=local; lang=zh_CH; loginUserId=100301"
        return cookie


