'''
Author: whalefall
Date: 2021-06-29 14:49:14
LastEditTime: 2021-06-29 15:14:13
Description: 鼠标操作
'''
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标操作类
from selenium.webdriver.common.keys import Keys

# 定义驱动地址
qudo = r"C:\Users\Administrator\Desktop\chromedriver.exe"
# 加载对应浏览器的驱动
wb = webdriver.Chrome(executable_path=qudo)
url = 'https://baidu.com/'
wb.get(url)
wb.maximize_window()
above = wb.find_element_by_xpath(r"//*[@id='s-usersetting-top']")
ActionChains(wb).move_to_element(above).perform()

wb.find_element_by_xpath(r"//*[@id='s-usersetting-top']").send_keys(Keys.SEMICOLON)