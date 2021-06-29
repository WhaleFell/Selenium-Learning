'''
Author: whalefall
Date: 2021-06-29 14:19:20
LastEditTime: 2021-06-29 14:34:33
Description: 基本操作
'''
from selenium import webdriver
from time import sleep

# 定义驱动地址
qudo = r"C:\Users\Administrator\Desktop\chromedriver.exe"
# 加载对应浏览器的驱动
wb = webdriver.Chrome(executable_path=qudo)
# 无头浏览器(节省内存)
# webdriver.PhantomJS()

# 访问url
wb.get("https://baidu.com/")

# 设置浏览器的长和宽
wb.set_window_size(500,600)
# 设置浏览器最大
wb.maximize_window()

# 找到文本框输入数值
wb.find_element_by_id('kw').send_keys("test")
# 找到按钮点击
# wb.find_element_by_id('su').click()
# 前进 后退页面
wb.back()
wb.forward()
# 刷新界面
wb.refresh()
# 基本操作
wb.find_element_by_id('su').click()
wb.find_element_by_id('su').clear()
wb.find_element_by_id('su').send_keys()
wb.find_element_by_id('su').submit() # 提交

sleep(8)
# 关闭浏览器
wb.quit()

