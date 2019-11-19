import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
from bs4 import BeautifulSoup
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

istate=-1
firebase=firebase.FirebaseApplication("https://iphack.firebaseio.com/",None)
cred = credentials.Certificate("iphack-firebase-adminsdk-vvh46-1889b9f306.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://iphack.firebaseio.com/users'})

def listener(event):
    import time
    global istate
    if istate == -1:
        istate = 0
    elif istate == 0:
        istate = 1
        fh = open('exam_data3.txt', 'a')
        st = '\n'
        fh.write(st)
        driver = webdriver.Chrome('/home/vinyas/Desktop/police_hackathon/chromedriver')
        driver.get("https://www.facebook.com")

        # getIn = input()

        driver.set_page_load_timeout(3600000)
        driver.implicitly_wait(360000)

        time.sleep(1)

        src1 = driver.page_source
        ele11 = bs4.BeautifulSoup(src1, "lxml")
        summery = ele11.get_text()
        if not summery.__contains__("It's quick and easy"):
            print(summery)
            ele1 = driver.find_element_by_name("email")
            ele2 = driver.find_element_by_name("pass")
            # ele1.clear()

            ele1.send_keys('')
            # ele2.clear()

            ele2.send_keys('')
            ele2.send_keys(Keys.ENTER)


        else:
            ele = driver.find_element_by_id('email')
            ele.clear()
            ele.send_keys('')

            ele = driver.find_element_by_id('pass')
            ele.clear()
            ele.send_keys('')

            ele.send_keys(Keys.ENTER)

        time.sleep(0.5)

        # username = 'Appasaheb Chavan'
        username=firebase.get('/name',None)
        # firebase.put('','/users/'+usr+'/instagram_state',"true")

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
        c=1
        for k in result_aTag.find_all('a', href=True):
            aHref = str(k['href'])
            if aHref.__contains__('https://www.facebook.com/' + username[0].lower()) and not (
                    aHref.__contains__('https://www.facebook.com/pages') or aHref.__contains__(
                    'https://www.facebook.com/profile')):
                result_links.append(k['href'])

        #print(result_links)
        #print('###########\n\n\n')

        data_remove = ['Edit your education', 'Edit your work', ]
        result_links=list(set(result_links))
        for k in result_links:
            data_overview = []
            data_education = []
            data_contact = []
            posts={}
            #profile_pic = timeline_src.find_all("div", {"class": "_66lg"}).a['href']
            driver.get(k + '/about')
            src = driver.page_source
            about_src = bs4.BeautifulSoup(src, 'lxml')
            profile_pic = about_src.find("img", {"class": "_11kf"})['src']
            #print(profile_pic)
            overview = about_src.select('.clearfix._5y02')
            #print(k)

            for k1 in overview:
                #print(k1.get_text())
                data_overview.append(k1.get_text())

            driver.get(k + '/about?section=education')
            # src = driver.page_source
            # about_src = bs4.BeautifulSoup(src, 'lxml')

            overview = about_src.select('._42ef')
            # print(k)

            for k1 in overview:
                #print(k1.get_text())
                data_education.append(k1.get_text())

            driver.get(k + '/about?section=contact')
            # src = driver.page_source
            # about_src = bs4.BeautifulSoup(src, 'lxml')

            overview = about_src.select('.clearfix._ikh')
            #print('##########Contact##########')

            for k1 in overview:
                #print(k1.get_text())
                data_contact.append(k1.get_text())

            driver.get(k+'/timeline')
            src = driver.page_source
            timeline_src = bs4.BeautifulSoup(src, 'lxml')
            outside_likes=timeline_src.select("._66lg")
            outside_name=timeline_src.select(".profileLink")
            outside_time=timeline_src.select(".timestampContent")

            time=outside_time[0].text
            like_link=outside_likes[0].a['href']
            driver.get("https://www.facebook.com"+like_link)
            src = driver.page_source
            like_src = bs4.BeautifulSoup(src, 'lxml')
            like_list=like_src.select("._5j0e.fsl.fwb.fcb")
            friends=[]
            for x in like_list:
                friends.append(x.text)
            posts[0]={"last_post_time ":time,"top_related_friends":friends}
            #print(posts)
            data_overview = " ".join(data_overview)
            data_education = " ".join(data_education)
            data_contact = " ".join(data_contact)
            data={}
            data={"name":username,"profile_image":profile_pic,"data_overview":data_overview,"data_education":data_education,"data_contact":data_contact,"recent_posts":posts}
            # c+=1
            # for i in range(1,c):
            #     print(data[i])
            # for i in range(1, len(data.keys()) + 1):
            firebase.put("", "/users/" + username + '/facebook/' + str(c), data)
            firebase.put("", "/users/" + username + '/facebook_state', "false")    #time.sleep(2)
            c=c+1
        istate=0
    else:
        abbs=1

    #driver.close()

ref = firebase_admin.db.reference('/name')
ref.listen(listener)
