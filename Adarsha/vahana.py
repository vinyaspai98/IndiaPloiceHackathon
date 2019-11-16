from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
import bs4

driver = webdriver.Chrome('/home/adarsha/Projects/hackathon-IPH-master/Adarsha/chromedriver')
driver.get('https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml')
time.sleep(20)
src=driver.page_source

r_src = bs4.BeautifulSoup(src, 'lxml')
r_div=r_src.find("div",{"class":"ui-outputpanel ui-widget"})
rtext=r_div.get_text()
print(type(rtext))