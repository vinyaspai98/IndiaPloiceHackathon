from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
from bs4 import BeautifulSoup
from firebase import firebase
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
import firebase_admin
from firebase import firebase
from firebase_admin import credentials
from firebase_admin import db
firebase = firebase.FirebaseApplication('https://iphack.firebaseio.com/', None)
cred = credentials.Certificate("iphack-firebase-adminsdk-vvh46-1889b9f306.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://iphack.firebaseio.com/users'})
nstate=-1
def listener(event):
    global nstate
    a_li=[]
    a_he=[]
    if nstate==-1:
        nstate=0
    elif nstate==0:
        nstate=1
        driver = webdriver.Chrome('/home/adarsha/Projects/hackathon-IPH-master/Adarsha/chromedriver')
        driver.get('https://news.google.com/?hl=en-IN&gl=IN&ceid=IN%3Aen')
        kword=firebase.get('/name',None)
        squery = driver.find_element_by_xpath("//input[@aria-label='Search']")
        squery.send_keys(kword)
        squery.send_keys(Keys.ENTER)
        time.sleep(3)
        src = driver.page_source
        rsrc = bs4.BeautifulSoup(src, 'lxml')
        an_sr=rsrc.select('.DY5T1d')
        c=0
        for ne in an_sr:
            nz=ne['href']
            nz=nz[1:]
            a_li.append("https://news.google.com"+nz)
            a_he.append(ne.text)
            c=c+1
            if c>5:
                break
        firebase.put('','/users/'+kword+'/news',{'link':a_li,'headline':a_he})
        firebase.put('','/users/'+usr+'/news_state',"false")
    else:
        asdf=2
time.sleep(0.01)
ref = firebase_admin.db.reference('/name')
ref.listen(listener)
