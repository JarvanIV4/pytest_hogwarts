ENV = "ST"

login_web_st = "http://www.baidu.com"
login_web_uat = "http://www.2345.com"

login_web = login_web_st if ENV=="ST" else login_web_uat