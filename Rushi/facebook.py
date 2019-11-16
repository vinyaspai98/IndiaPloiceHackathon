import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
from bs4 import BeautifulSoup


import time


fh = open('exam_data3.txt','a')
st = '\n'
fh.write(st)
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

# getIn = input()

driver.set_page_load_timeout(360000)
driver.implicitly_wait(360000)


time.sleep(1)

ele = driver.find_element_by_id('email')
ele.clear()
ele.send_keys('76766555676')

ele = driver.find_element_by_id('pass')
ele.clear()
ele.send_keys('Appasaheb%1117')

ele.send_keys(Keys.ENTER)


time.sleep(0.5)

# username = 'Rushikesh Chavan'
# ele = driver.find_element_by_class_name('_1frb')
# ele.clear()
# ele.send_keys('Rushikesh Chavan')


# ele.send_keys(Keys.ENTER)


# time.sleep(2)

# print('hey')
# src = driver.page_source
# results_src = bs4.BeautifulSoup(src, 'lxml')  # loading the attandance page

# result_div = results_src.select('._1yt')
# result_aTag = result_div[0]
# result_links = []
# for k in result_aTag.find_all('a',href=True):
#     aHref = str(k['href'])
#     if aHref.__contains__('https://www.facebook.com/'+username[0].lower())  and not (aHref.__contains__('https://www.facebook.com/pages') or aHref.__contains__('https://www.facebook.com/profile')):
#         result_links.append(k['href'])


# print(result_links)

# for k in result_links:
driver.get('https://www.facebook.com/rushirushirushi/about')
src = driver.page_source
about_src = bs4.BeautifulSoup(src, 'lxml')

overview = about_src.select('.clearfix._5y02')
# print(overview)

for k in overview:
    # span = k.find_all('span')
    print(k.get_text())
    # print('###########')

    



time.sleep(2)

driver.close()