# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import unittest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 按住ctrl,点击sys,将以下两行代码复制到sys.py文件末尾
# def setdefaultencoding(param):
#     return None
'''
驱动程序
运行思路:
1>获取脚本的存放位置
2>获取将要运行的脚本,并将其加入测试集
3>运行脚本,调用data中的数据
4>生成测试报告存入report下
5>邮件设计,并给项目组成员发邮件
'''
def getSuite():
    # 1>获取脚本存放位置
    test_dir = 'E:\\python_workspace\\appium-framework-week4\\scripts'
    # 2>获取将要运行的脚本,并将其加入测试集
    # discover(参数1,参数2)
    # 参数1:脚本存放位置  test_dir
    # 参数2:脚本格式pattern,以test开头的.py结尾的文件  test*.py
    discov = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # 将获取的脚本加入测试集
    suite = unittest.TestSuite()
    # 遍历循环discov中的用例,加入suite中
    for testcase in discov:
        suite.addTest(testcase)
    # 返回测试集
    return suite


# 4>设计报告
def designReport():
    global runner
    global file_rt
    global report_name
    # 将HTMLTestRunner.py放置C:\Python27\Lib下
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    # .表示当前目录
    # 生成的报告文件路径
    report_name = ".\\report\\" + now + "result.html"
    print(report_name)
    file_rt = open(report_name, 'wb')  # wb二进制写入方式
    # stream:打开的报告文件名
    # title:报告的标题
    # description:测试执行结果的描述
    runner = HTMLTestRunner(stream=file_rt, title='appium_youdao_test', description='测试结果如下')


# 5>发送邮件
def sendEmail(rt):
    f = open(rt, 'rb')  # 二进制读的方式打开
    # 将报告作为邮件正文
    mail_body = f.read()
    msg = MIMEText(mail_body, 'html', 'utf-8')  # 给邮件规定格式
    msg['Subject'] = Header('appium手机自动化测试报告-week4', 'utf-8')  # 主题
    msg['From'] = 'bszhangf@126.com'  # 发件人
    msg['To'] = '18401569214@163.com'  # 收件人,收件人为多个,用分号隔开
    smtp = smtplib.SMTP('smtp.126.com')
    smtp.login('bszhangf@126.com', 'song3143723177')  # 邮箱登录用户名和密码
    # smtp.sendmail('15032683126@163.com', '18401569214@163.com', msg.as_string())
    smtp.sendmail(msg['From'],msg['To'].split(';'),msg.as_string())
    smtp.quit()   # 退出邮箱服务器
    print('------邮件发送成功-------')



#6> 调用 -- 运行驱动
suites = getSuite()
designReport()
runner.run(suites)
file_rt.close()
sendEmail(report_name)