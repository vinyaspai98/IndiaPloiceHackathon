from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
istate=-1
firebase=firebase.FirebaseApplication("https://iphack.firebaseio.com/",None)
cred = credentials.Certificate("iphack-firebase-adminsdk-vvh46-1889b9f306.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://iphack.firebaseio.com/users'})
def listener(event):
    try:
        global istate
        if istate==-1:
            istate=0
        elif istate==0:
            istate=1
            data={}
            driver = webdriver.Chrome('/home/vinyas/Desktop/police_hackathon/chromedriver')
            driver.get('https://www.instagram.com/accounts/login/')
            print("Opened instagram...")

            #dom = driver.find_element_by_xpath('//*')
            time.sleep(2)
            email = driver.find_element_by_xpath('//input[@name="username"]')
            email.send_keys('eagleeye.iph@gmail.com')
            print("email entered...")
            password = driver.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
            password.send_keys('qwerty#123')
            print("Password entered...")
            button = driver.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]")
            button.click()
            print("instagram opened")
            time.sleep(3)
            status = driver.find_element_by_xpath("/html/body/span/section/nav/div[2]/div/div/div[2]/input")
            usr=firebase.get('/name',None)
            # firebase.put('','/users/'+usr+'/instagram_state',"true")
            status.send_keys(usr)
            status.send_keys(Keys.ENTER)
            print("Status trying")
            #postbutton = driver.find_element_by_xpath("//button[contains(.,'Post')]")
            #postbutton.click()
            time.sleep(2)
            src = driver.page_source
            results_src = BeautifulSoup(src, 'lxml')  # loading the attandance page
            result_div = results_src.select('.yCE8d  ')
            #print(result_div)
            dc=1
            c=1
            for k in result_div:
                image=""
                handle_name=""
                bio=""
                bio_name=""
                result_aTag = k['href']
                #print(result_aTag)
                driver.get('https://www.instagram.com'+str(result_aTag))
                time.sleep(2)
                src_per_page = driver.page_source
                results_src_per_page = BeautifulSoup(src_per_page, 'lxml')  # loading the attandance page
                result_div_header = results_src_per_page.select('.vtbgv  ')
                for j in result_div_header:
                    bio_name = results_src_per_page.find('h1', attrs={'class': 'rhpdm'}).text
                    s=str(j.get_text())
                    image=k.find('img')['src']
                    handle_name=s[0:s.find('Follow')]
                    bio=s[s.find('following')+9:]
                    bio=bio[len(bio_name):]
                    #bio_name = results_src_per_page.find('h1', attrs={'class': 'rhpdm'}).text
                try:
                    print("=====================================================")
                    print(image)
                    print(handle_name)
                    print(bio)
                    print(bio_name)
                    print("================================================")
                except:
                    asdsaf=1
                if(image != "" and handle_name != "" and bio != "" and bio_name != "" ):
                    data[dc]={"profile_image":image,"handle_name":handle_name,"name":bio_name,"bio":bio}
                    dc+=1
                elif(image != "" and handle_name != "" and bio_name != ""):
                    data[dc] = {"profile_image": image, "handle_name": handle_name, "name": bio_name, "bio": bio}
                    dc+=1
                c+=1
                if c==7:
                    break
            #print(data)
            for i in range(1,len(data.keys())+1):
                firebase.put("","/users/"+usr+'/instagram/'+str(i),data[i])
                firebase.put("","/users/"+usr+'/instagram_state',"false")
            print("post done")
            istate=0
        else:
            asdsfds=1
    except:
        pass
ref = firebase_admin.db.reference('/name')
ref.listen(listener)
