# coding=utf-8
import unittest
from appium import webdriver
import time
from selenium.webdriver.common.by import By

from scripts.public.exit_app import exitApp


class Bself(unittest.TestCase):
    # 云笔记标签与我的标签切换
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

        def test_bself(self):
            driver = self.driver
            time.sleep(3)
            # 截图1
            driver.get_screenshot_as_file('E:\\python_workspace\\appium-framework-week4\\picture\\picture1.png')
            # 我的
            driver.find_element(By.NAME, '我的').click()
            time.sleep(2)
            # 截图2
            driver.get_screenshot_as_file('E:\\python_workspace\\appium-framework-week4\\picture\\picture2.png')
            # 点击云协作
            driver.find_element(By.NAME, '云协作').click()
            time.sleep(2)
            # 截图3
            driver.get_screenshot_as_file('E:\\python_workspace\\appium-framework-week4\\picture\\picture3.png')

        def tearDown(self):
            exitApp(self)