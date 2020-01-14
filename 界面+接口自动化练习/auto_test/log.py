# coding:utf-8
#python中生成日志的包
import logging
import time

"""
配置日志打印级别
"""
class log():
    def __init__(self,name):
        #初始化日志文件名
        self.logname = name

    def setMsg(self,level,msg):
        logpath = r"E:\ProgramData\python_work\auto_test\ui_test\log\\"
        # now = time.strftime("%y-%m-%d_%H-%M-%S",time.localtime())
        lname = logpath+self.logname
        logger = logging.getLogger() #获取日志实例
        fh = logging.FileHandler(lname)  #定义日志写入的文件
        ch = logging.StreamHandler()     #定义日志在控制台输出
        #定义日志输出的格式位 时间 日志等级:日志信息
        fmt = logging.Formatter("%(asctime)s %(levelname)-8s:%(message)s")
        #分别给文件日志和控制台日志设置刚才设定的日志格式
        fh.setFormatter(fmt)
        ch.setFormatter(fmt)
        #添加haddler,为日志添加日志处理器
        logger.addHandler(fh)
        logger.addHandler(ch)
        #添加日志信息，输出INFO级别的日志信息
        logger.setLevel(logging.INFO)
        """
        对输入的的参数进行判断，例如输入的level等级为info
        则调用logger中的info方法将日志信息写入到文件中
        """
        if level == "debug":
            logger.debug(msg)
        elif level == "info":
            logger.info(msg)
        elif level == "warning":
            logger.warning(msg)
        elif level == "error":
            logger.error(msg)
        #移除日志输出平台，避免重复写入
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()
    def debug(self,msg):
        self.setMsg('debug',msg)
    def info(self,msg):
        self.setMsg("info",msg)
    def warning(self,msg):
        self.setMsg("warning",msg)
    def error(self,msg):
        self.setMsg("error",msg)
if __name__ == '__main__':
    l = log("execute.log")
    l.error("practice")
    l.info("test2")
        
