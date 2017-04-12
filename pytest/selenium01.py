# coding=utf-8
'''
selenium 测试
'''
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains  # 引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys  # 引入keys类操作
from selenium.webdriver.support.ui import WebDriverWait

__author__ = "wtj"


def sleep(s):
    time.sleep(s)


def conUrl(url):
    # browser = webdriver.Firefox() # Get local session of firefox
    browser = webdriver.Chrome()
    browser.get(url)  # Load page
    print('goto:url=' + url)
# assert "Yahoo!" in browser.title
    print(browser.find_element_by_id('jgwab').text)
    elem = browser.find_element_by_name("wd")  # Find the query box
    # print(browser.find_element_by_id('wd'))  # 打印输入框的大小
    elem.send_keys("徐家汇商城" + Keys.RETURN)
    sleep(0.2)  # Let the page load, will be added to the API
    # browser.set_window_size(500, 500)
    # sleep(1)
    # browser.back()
    # sleep(1)
    # browser.forward()
    # sleep(1)
    print(browser.window_handles)
    _winhandle=browser.current_window_handle
    try:
        # xjhElem = browser.find_elements_by_xpath(
        #     "//a[contains(@href,'http://www.baidu.com/link?url=Hekhd8lwjJ8DqfvTqgoY2D5ZBWFJV-L_acY2Xqy4fNW')]")
        xjhElem = browser.find_element_by_css_selector('.result  h3 a').click()
        # print(xjhElem)
        # ActionChains(browser).click(xjhElem).perform()
        # sleep(1)
        print(browser.title)
        allhandles = browser.window_handles
        for  han in allhandles:
        	if han!=_winhandle:
        		browser.switch_to_window(han)#前面click打开了一个新的窗口。这边选择这个窗口
        print(browser.window_handles)
        # now_handle = browser.current_window_handle
        print(browser.current_window_handle)
        new_dom = WebDriverWait(browser, 60).until(lambda x: x.find_element_by_id(
            "login"))
        new_dom.click()
        print(browser.current_window_handle)
        print(new_dom)
        sleep(20)
    except NoSuchElementException:
        assert 0, "error"
        browser.close()


if __name__ == '__main__':
    conUrl("http://www.baidu.com")
