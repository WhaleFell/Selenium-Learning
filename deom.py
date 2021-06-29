'''
Author: whalefall
Date: 2021-06-29 16:57:03
LastEditTime: 2021-06-29 17:42:02
Description: 爬取句子迷首页金句
'''
from selenium import webdriver
from time import sleep

qudo = r"C:\Users\Administrator\Desktop\chromedriver.exe"

wb = webdriver.Chrome(qudo)
url = "https://www.juzikong.com/"
wb.get(url)
# elements = wb.find_elements_by_xpath(
#     r'//*[@id="__layout"]//p/a/span')
# for element in elements:
#     print(element.text.replace("\n",","))
sleep(8)
for i in range(1, 200):
    # wb.find_element_by_tag_name('button').click()
    wb.find_element_by_class_name('loadmore_ZcRdW').click()
    sleep(0.5)
    wb.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("第%s点击" % (i))
# wb.find_element_by_xpath(r'//*[@id="__layout"]//button').click()
# wb.find_element_by_partial_link_text("点击加载更多").click()
# wb.find_element_by_tag_name('button').click()

elements = wb.find_elements_by_xpath(
    r'//*[@id="__layout"]//p/a/span')

for element in elements:
    print(element.text.replace("\n",","))

# wb.save_screenshot('test.png')

# sleep(3)
# wb.quit()
