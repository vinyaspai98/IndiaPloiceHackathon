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
#from selenium.webdriver.chrome.options import Options
#opts = Options()
#opts.add_argument("user-agent=whatever you want")

#driver = webdriver.Chrome(chrome_options=opts)
driver = webdriver.Chrome('/home/adarsha/Projects/hackathon-IPH-master/Adarsha/chromedriver')
driver.get('https://www.truecaller.com')
print("Opened facebook...")
email = driver.find_element_by_xpath("//input[@aria-label='Phone number']")
email.send_keys('7338324602')
button = driver.find_element_by_xpath("//button[@aria-label='Search']")
button.click()
time.sleep(5)
continue_link = driver.find_element_by_link_text('Sign in with Google')
continue_link.click()

email1 = driver.find_element_by_xpath("//input[@type='email']")
email1.send_keys('benkibasya@gmail.com')
#content = driver.find_element_by_class_name('RveJvd')
#content.click()
time.sleep(10)
email1.send_keys(Keys.ENTER)
time.sleep(10)
fpass = driver.find_element_by_name('password')
time.sleep(12)
fpass.send_keys('qwerty#123')
fpass.send_keys(Keys.ENTER)
time.sleep(17)
src = driver.page_source

#f=open("hi.txt","r")
#html_doc=f.read()
results_src = bs4.BeautifulSoup(src, 'lxml')  # loading the attandance page

#for a in results_src.find_all('a', href=True):
#print("Found the URL:", a['href'])
#print(results_src)
try:
    ress=results_src.find("img",{"class":"object-cover w-24 h-24 rounded-full"})
    print("image link is :",ress.src)
except:
    print("image link not found")
try:
    result = results_src.find("div", {"class":"flex-1 w-full text-xs text-fontSecondaryColor truncate pr-4"})
    print(result.text)
except:
    print("exception happenned in carrier provider")
try:
    result1 = results_src.find_all("div", {"class":"flex-1 h-16 leading-16 border-b border-borderColor truncate pr-4"})
    if len(result1)==1:
        print("email id not found")
        print("location is :",result1[0].text)
    else:
        print("email id is :",result1[0].text)
        print("location is :",result1[1].text)

except:
    print("didn't get email and location")
