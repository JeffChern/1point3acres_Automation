
# coding: utf-8

from selenium import webdriver
import time

chrome_path = '__YOUR__CHROME_DRIVER_PATH__'
browser = webdriver.Chrome(chrome_path)
browser.get('http://www.1point3acres.com/bbs/')
browser.find_element_by_id("ls_username").send_keys("__USERNAME__")
browser.find_element_by_id("ls_password").send_keys("__PASSWORD__")
time.sleep(5)
browser.find_element_by_css_selector("button.pn.vm").click()
browser.find_element_by_xpath("//div[@id='um']/p/a[4]/font").click()
time.sleep(3)
browser.find_element_by_css_selector("#fd > center > img").click()
time.sleep(3)
browser.find_element_by_xpath("(//input[@name='qdmode'])[2]").click()
time.sleep(3)
browser.find_element_by_css_selector("button.pn.pnc").click()

browser.quit()




