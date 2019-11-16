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

username = 'Appasaheb Chavan'
driver.get('https://www.facebook.com/search/top/?q=' + username.replace(' ', '%') + '&epa=SEARCH_BOX')
# time.sleep(2)
# ele = driver.find_element_by_class_name('_1frb')
# ele.clear()
# ele.send_keys('Rushikesh Chavan')


# ele.send_keys(Keys.ENTER)


time.sleep(0.5)

print('hey')
src = driver.page_source
results_src = bs4.BeautifulSoup(src, 'lxml')  # loading the attandance page

result_div = results_src.select('._1yt')
result_aTag = result_div[0]
result_links = []
for k in result_aTag.find_all('a',href=True):
    aHref = str(k['href'])
    if aHref.__contains__('https://www.facebook.com/'+username[0].lower())  and not (aHref.__contains__('https://www.facebook.com/pages') or aHref.__contains__('https://www.facebook.com/profile')):
        result_links.append(k['href'])


print(result_links)
print('###########\n\n\n')

data_remove = ['Edit your education','Edit your work',]
data_overview = []
data_education = []
data_contact = []
for k in result_links:
    driver.get(k+'/about')
    src = driver.page_source
    about_src = bs4.BeautifulSoup(src, 'lxml')

    overview = about_src.select('.clearfix._5y02')
    print(k)

    for k1 in overview:
        print(k1.get_text())
        data_overview.append(k1.get_text())

    driver.get(k+'/about?section=education')
    # src = driver.page_source
    # about_src = bs4.BeautifulSoup(src, 'lxml')

    overview = about_src.select('._42ef')
    # print(k)

    for k1 in overview:
        print(k1.get_text())
        data_education.append(k1.get_text())
    
    
    driver.get(k+'/about?section=contact')
    # src = driver.page_source
    # about_src = bs4.BeautifulSoup(src, 'lxml')

    overview = about_src.select('.clearfix._ikh')
    print('##########Contact##########')

    for k1 in overview:
        print(k1.get_text())
        data_contact.append(k1.get_text())


time.sleep(2)

driver.close()