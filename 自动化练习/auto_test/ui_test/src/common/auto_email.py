# coding:utf-8
import smtplib    #邮件发送的核心类
from email.mime.text import MIMEText  #初始化邮件内容
from email.header import Header   #初始化邮件头部信息
from email.mime.multipart import MIMEMultipart  #附件


class auto_email():
    def __init__(self):
        self.mail_host = "smtp.qq.com"    #配置邮件发送服务，例如qq邮箱：smtp.qq.com
        self.mail_user = "2268035948@qq.com"   #邮件发送者账号
        self.mail_password = "jtyatearwxzgeaib"     #发送邮箱的授权码
        self.sender = "2268035948@qq.com"    #与发送者相同
        self.reciver = "18708730832@163.com"  #邮件接收者
    def send_email(self,report):
        # report = "auto_test.html"
        with open(report,"rb") as f:  #打开指定文件，以二进制的方式打开
            mail_content = f.read()
        # text_msg = MIMEText(mail_content,"plain","utf-8")
        text_msg = MIMEText(mail_content,"html","utf-8")  #配置邮件内容
        text_msg["Content_Type"] = "application/octet-stream" #配置邮件类型，默认写法
        text_msg["Content-Dispostion"] = '自动化测试报告'
        #创建一个带附件的邮件实例,作为根容器
        main_msg = MIMEMultipart()
        #将邮件显示内容添加到根容器
        main_msg.attach(text_msg)
        main_msg["From"] = self.sender   #配置邮件发送方
        main_msg["To"] = self.reciver    #配置邮件接收方
        # main_msg.attach(MIMEText(mail_content,"html","utf-8"))
        subject = "good good study day day up"  #配置邮件主题
        main_msg["Subject"] = Header(subject,"utf-8")
        try:
            smtpobj = smtplib.SMTP_SSL(self.mail_host,465)  #配置发送端口及邮件服务
            smtpobj.login(self.mail_user,self.mail_password)  #配置邮箱登录名及授权码
            smtpobj.sendmail(self.sender,self.reciver,main_msg.as_string())  #配置邮件内容
            smtpobj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(e)
if __name__ == '__main__':
    ae = auto_email()  #创建类的对象
    report = r"D:\python_work\auto_test\report\AutoTest2019-01-21_20-36-02_05 list_dict_test.html"
    ae.send_email(report)  #调用发送邮件的方法，传入参数为路径+文件名

    #535错误：邮箱登录，认证失败，授权码与登录用户名不符
    #554错误：邮件内容或主题被频繁使用，被系统识别为非法邮件，需要修改主题或内容