# coding=utf-8

import unittest
from appium import webdriver
import time
from selenium.webdriver.common.by import By
import xlrd

from scripts.public.exit_app import exitApp


class Anewnote(unittest.TestCase):
    '''新建云笔记'''
    # '''三引号可以在报告中加入中文
    def setUp(self):
        desired_caps = {
            'platformName' : 'Android',
            'platformVersion' : '4.4.2',
            'deviceName' : '127.0.0.1:22515',
            'appPackage' : 'com.youdao.note',
            'appActivity' : '.activity2.SplashActivity',
            'unicodeKeyboard' : 'True', # 防止键盘中文不能输入
            'resetKeyboard' : 'True'  # 重置设置生效
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_newnote(self):
        driver = self.driver
        time.sleep(3)

        # 1>打开excel
        wb = xlrd.open_workbook("E:\\python_workspace\\appium-framework-week4\\data\\data-week4.xls")
        # 2>获取sheet页note
        sh = wb.sheet_by_name("note")

        r_num = sh.nrows
        for i in range(1, r_num):
            title = sh.cell_value(i, 1)
            content = sh.cell_value(i, 2)
            expect = sh.cell_value(i, 3)

            # +号 官方推荐  By.ID
            driver.find_element(By.ID,  'com.youdao.note:id/add_note_floater_open').click()
            # 新建笔记
            driver.find_element(By.NAME, '新建笔记').click()
            # 标题
            driver.find_element(By.ID, 'com.youdao.note:id/note_title').send_keys(title)
            # 正文  输入内容为中文,前面加u
            driver.find_element(By.XPATH, '//android.widget.LinearLayout[@resource-id=\"com.youdao.note:id/note_content\"]/android.widget.EditText[1]').send_keys(content)
            # 完成
            driver.find_element(By.ID, 'com.youdao.note:id/actionbar_complete_text').click()
            # 验证
            if expect == 'ok':
                if driver.find_element(By.NAME, title) and driver.find_element(By.NAME, content):
                    print('success')
                else:
                    print('fail')
            elif title == '':
                res1 = driver.find_element(By.ID, 'com.youdao.note:id/title').text
                res2 = driver.find_element(By.ID, 'com.youdao.note:id/summary').text
                if res1 == res2:
                    print('success')
                else:
                    print('fail')
            elif expect == 'tit':
                if driver.find_element(By.NAME, title):
                    print('success')
                else:
                    print('fail')

    def tearDown(self):
        # 退出app
        exitApp(self)