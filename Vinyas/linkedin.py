from selenium import webdriver
import bs4
import json
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome('/home/vinyas/Desktop/police_hackathon/chromedriver')
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
email = driver.find_element_by_xpath("/html/body/div/main/div/form/div[1]/input")
email.send_keys('vinyaspai98@gmail.com')
password = driver.find_element_by_xpath("/html/body/div/main/div/form/div[2]/input")
password.send_keys('vinnu1998')
button = driver.find_element_by_xpath("/html/body/div/main/div/form/div[3]/button")
button.click()
time.sleep(25)
search=driver.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[1]/div/input")
search.send_keys("vinyas")
ppl = driver.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[2]/button")
ppl.click()
time.sleep(2)
ele=driver.page_source
src=bs4.BeautifulSoup(ele,'lxml')
# print(src)
p=src.select('.search-results__list')
pp=p[0].select('li')
# print(pp)
people=[]
url="https://www.linkedin.com"
for k in pp:
    k1=k.select('.search-result__wrapper')
    if(len(k1)==0):
        continue
    a=k1[0].find_all('a',href=True)
    ahref=a[1]['href']
    print(ahref)
    # print(k1)
    print("######")
    driver.get(url+ahref)
    time.sleep(2)
    ele1 = driver.page_source
    src1 = bs4.BeautifulSoup(ele1, 'lxml')
    name = src1.find("li", {"class": "inline t-24 t-black t-normal break-words"})
    name1=""
    bio1=""
    loc1=""
    abt1=""
    name1=name.text.strip()
    # print("Name:"+name1)
    work=src1.find_all("span",{"class":"text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view"})
    w1=[]
    for w in work:
        w1.append(w.text.strip("\n"))
    # print(w1)
    bio=src1.find("h2",{"class":"mt1 t-18 t-black t-normal"})
    if bio:
        bio1=bio.text.strip()
        # print(bio1)
    loc=src1.find("li",{"class":"t-16 t-black t-normal inline-block"})
    if loc:
        loc1=loc.text.strip()
        # print(loc.text.strip())

    abt=src1.find("span",{"class":"lt-line-clamp__raw-line"})
    if abt:
        abt1=abt.text.strip()
        # print(abt.text.strip())
    # exp=[]
    # e=src.find_all("ul",{"class":"pv-profile-section__section-info section-info pv-profile-section__section-info--has-no-more"})
    # if(len(e)):
    #     for i in e:
    #         ee = i.find("h3", {"class": "t-16 t-black t-bold"}).text.strip()
    #         print(ee)
    #         p = i.find_all("p", {"class": "pv-entity__secondary-title t-14 t-black t-normal"})
    #         b = []
    #         for pp in p:
    #             b = b + " " + pp.text.strip()
    #         print(b)
    #         c = []
    #         p = i.find_all("h4", {"class": "pv-entity__date-range t-14 t-black--light t-normal"})
    #         for pp in p:

    #             c = c + " " + pp.text.strip()
    #         print(c)
    # for i in lang:
    #     print(i.get_text())
    # interests=src1.find("li", {"class":"pv-accomplishments-block__summary-list-item"})
    # print(interests)
    edu=""
    wo=""
    if(len(w1)==1):
        edu=w1[0]
        wo=""
    if(len(w1)==2):
        edu=w1[1]
        wo=w1[0]
    x={
        "name":name1,
        "work":wo,
        "education":edu,
        "bio":bio1,
        "location":loc1,
        "about":abt1

    }
    print(x)


driver.close()