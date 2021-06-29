'''
Author: whalefall
Date: 2021-06-29 12:31:22
LastEditTime: 2021-06-29 14:15:40
Description: selenium 自动化测试学习
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

# 找到文本框输入数值
# wb.find_element_by_id('kw').send_keys("test")
# 找到按钮点击
# wb.find_element_by_id('su').click()

# 更多查找
# wb.find_element_by_name()  # name名查找
# wb.find_element_by_tag_name()  # tag名查找
# wb.find_element_by_class_name()  # 通过Class名查找
# wb.find_element_by_link_text()  # 通过完整的链接文本查找
# wb.find_element_by_partial_link_text()  # 通过模糊的链接文本查找
# wb.find_element_by_xpath()  # 通过xpath名查找
# wb.find_element_by_css_selector()  # 通过CSS查找

elements = wb.find_elements_by_class_name('title-content-title')
for element in elements:
    print(element.text)


sleep(8)
# 关闭浏览器
wb.close()
