from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
data={}
driver = webdriver.Chrome('C:\\Users\\lenovo\\PycharmProjects\\IPH\\chromedriver')
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
status.send_keys("adarsha")
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
    img=""
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
    result_div_body = results_src_per_page.find('div',attrs={'class': '_4Kbb_ _54f4m'})
    if(result_div_body != None):
        existance="the account is either private or the user has not posted any image"
    result_div_body = results_src_per_page.find('div', attrs={'class': 'fx7hk'})
    if (result_div_body != None):
        existance = "the account has image"
        time.sleep(1)
        image_button = driver.find_element_by_xpath("/html/body/span/section/main/div/div[3]/article[2]/div/div/div[1]/div[1]/a")
        image_button.click()
        likers_set = results_src_per_page.find_all('div', attrs={'class': '                  Igw0E     IwRSH      eGOV_        vwCYk                                                                            i0EQd                                   '})
        print(likers_set)

    print("=====================================================")
    print(image)
    print(handle_name)
    print(bio)
    print(bio_name)
    print(existance)
    print("================================================")
    if(image != "" and handle_name != "" and bio != "" and bio_name != "" ):
        data[dc]={"profile_image":image,"handle_name":handle_name,"bio_name":bio_name,"bio":bio}
        dc+=1
    elif(image != "" and handle_name != "" and bio_name != ""):
        data[dc] = {"profile_image": image, "handle_name": handle_name, "bio_name": bio_name, "bio": bio}
        dc+=1
    c+=1
    if c==2:
        break
print(data)
print("post done")