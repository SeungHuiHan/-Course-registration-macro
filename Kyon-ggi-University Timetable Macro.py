#pip install selenium 설치
#python -m pip install bs4 설치
from lib2to3.pgen2.literals import evalString
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
 
browser = webdriver.Chrome("C:\chromedriver.exe") #chromedriver가 있는 파일 경로 입력
browser.get('http://sugang.kyonggi.ac.kr/')
browser.maximize_window()

browser.implicitly_wait(2)
while(True):
    browser.switch_to.frame("Main")

    browser.find_element_by_xpath('//*[@id="id"]').send_keys('202015333')

    browser.find_element_by_xpath('//*[@id="pwd"]').send_keys('gpfmaldhssm5')
    browser.find_element_by_id('btn_login').click()

    browser.implicitly_wait(2)
#da = Alert(browser)
#da.accept()

#browser.switch_to.frame("Main")
    browser.implicitly_wait(2)
    browser.switch_to.frame('coreMain')
    if browser.find_element_by_class_name('main.ui-button.ui-corner-all.ui-widget'):
        print("class있음")
    else: print("없음")

    browser.find_element_by_class_name('main.ui-button.ui-corner-all.ui-widget').send_keys(Keys.ENTER)
    browser.find_element_by_link_text('수강신청').send_keys(Keys.ENTER)
    time.sleep(2)
    a=0
    while a<48:
        browser.find_element_by_xpath('//*[@id="2"]/td[2]/button').send_keys(Keys.ENTER)
        da = Alert(browser)
        da.accept()
        browser.implicitly_wait(2)
        browser.find_element_by_xpath('/html/body/div[4]/div[3]/div/button').send_keys(Keys.ENTER)
        time.sleep(1)
        a+=1
    time.sleep(2)
    if browser.find_element_by_xpath('/html/body/div[3]/header/table/tbody/tr/td[2]/div/div/span[3]/button'):
        print("class있음")
    else: print("없음")
    element = browser.find_element_by_xpath("/html/body/div[3]/header/table/tbody/tr/td[2]/div/div/span[3]/button")
    browser.execute_script("arguments[0].click();", element)
#browser.find_element_by_xpath('/html/body/div[3]/header/table/tbody/tr/td[2]/div/div/span[3]/button').send_keys(Keys.ENTER)
    browser.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[1]').send_keys(Keys.ENTER)
    time.sleep(2)

while(True):
    pass
