# Selenium-Learning
> 学习 Python Selenium 自动化测试项目

## 前期准备

1. selenium 模块安装

```sh
pip install selenium
```

2. 安装浏览器驱动 `webdriver`

   驱动下载地址: [Chrome Driver](https://npm.taobao.org/mirrors/chromedriver/)

   **Google Chrom 浏览器**下载地址: [Chrome](https://www.google.com/intl/zh-CN/chrome/)

3. 加载浏览器驱动

   > 注意: 驱动版本要与浏览器版本相照应
   >
   > ![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210629122725.png)
   >
   > ![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210629122942.png)

   ![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210629121812.png)

   > 也可以把驱动路径加入**Path变量**

   > ## Selenium 原理
   >
   > ![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210629124034.png)

## selenium 元素的基本操作

> 寻找**元素的几大方式**

![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210629124148.png)

- **查找元素**

  ```python
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
  wb.find_element_by_id('kw').send_keys("test")
  # 找到按钮点击
  wb.find_element_by_id('su').click()
  
  sleep(8)
  wb.quit() # 关闭浏览器
  ```

- 更多定位元素方法

  ```python
  wb.find_element_by_name() # name名查找
  wb.find_element_by_tag_name() # tag名查找
  wb.find_element_by_class_name() # 通过Class名查找
  wb.find_element_by_link_text() # 通过完整的链接文本查找
  wb.find_element_by_partial_link_text() # 通过模糊的链接文本查找
  wb.find_element_by_xpath() # 通过xpath名查找
  wb.find_element_by_css_selector() # 通过CSS查找
  ```

- 定位一组元素
	``` Python
	elements = wb.find_elements_by_class_name('title-content-title')
	for element in elements:
    	print(element.text)
	```

## 基本操作

1. 设置浏览器尺寸

   ```python
   # 设置浏览器的长和宽
   wb.set_window_size(500,600)
   # 设置浏览器最大
   wb.maximize_window()
   ```

2. 前进 后退

   ```python
   # 前进 后退页面
   wb.back()
   wb.forward()
   ```

3. 刷新界面

   ```python
   # 刷新界面
   wb.refresh()
   ```

4. 清除,点击,输入

   ```python
   wb.find_element_by_id('su').click()
   wb.find_element_by_id('su').clear()
   wb.find_element_by_id('su').send_keys()
   wb.find_element_by_id('su').submit() # 表单提交
   ```

   ![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210629143735.png)

## 元素方法

![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210629144612.png)

## 鼠标操作

**在webdriver中，鼠标操作的方法封装在ActionChains类提供。ActionChains类提供 了鼠标操作的常用方法:**

ActionChains(driver),将浏览器驱动**driver作为参数传入**。
> (1) perform():执行所有ActionChains中存储的行为，是对整个操作的提交动作;
> (2) context_click(): 右击
> (3) double_click(): 双击
> (4) drag_and_drop(): 拖动
> (5) move_to_ element(): 鼠标悬停，在调用时需要指定元素定位

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标操作类
wb = webdriver.Chrome()
url = 'https://baidu.com/'
wb.get(url)
wb.maximize_window()
above = wb.find_element_by_xpath(r"//*[@id='s-usersetting-top']")
ActionChains(wb).move_to_element(above).perform()
```

## 键盘事件

 前面的send, keys()方法用来**模拟键盘输入**; keys() 类提供了键盘上几乎所有按键的方法，组合键也是可以的。
 常用的键盘操作如下:


> send_ keys(Keys.BACK. SPACE)删除键(BackSpace)
> send_ keys(Keys.SPACE) 空格键(Space)
> send_ keys(Keys.TAB) 制表键(Tab)
> send. _keys(Keys.ESCAPE)回退键(Esc)
> send_ keys(Keys.ENTER) 回车键(Enter)
> send_ keys(Keys.CONTROL,'a") 全选(Ctrl+A)
> send_ keys(Keys.CONTROL,'C")复制(Ctrl+C)
> send_ keys(Keys.CONTROL,'x') 剪切(Ctrl+X)
> send_ keys(Keys.CONTROL,'V') 粘贴(Ctrl+V)
> send_ keys(Keys.F1)键盘F1
> send_ keys(Keys.F12) 键盘F12

```python
from selenium.webdriver.common.keys import Keys
wb.find_element_by_xpath(r"//*[@id='s-usersetting-top']").send_keys(Keys.SEMICOLON)
```

