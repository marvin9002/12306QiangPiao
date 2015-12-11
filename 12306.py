#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from time import sleep
import traceback

ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
driver = webdriver.Firefox()
#print driver.current_url
def login(username,password):
           
           driver.find_element_by_id('login_user').click()
           sleep(3)
           loginname=driver.find_element_by_id('username')
           loginname.clear()
           loginname.send_keys(username)
           
           driver.find_element_by_id('password').send_keys(password)
           
           print "等待验证码，自行输入..."
           while True:                     
                      if driver.current_url != initmy_url:
                                 sleep(1)
                      else:
                                 break
def qiangpiao(username,password,from_station,to_station,time):
           driver.get(ticket_url)  
           while driver.find_element_by_id("login_user").is_displayed():
                      sleep(1)
                      login(username,password)    
                      if driver.current_url == initmy_url:
                                 print " 你已经成功登陆"
                                 break                      

           try:
                      print "购票页面..."
                      # 跳回购票页面
                      driver.get(ticket_url)
       
                      # 加载查询信息
                      WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_id('train_date').is_displayed())
                      driver.add_cookie({'name':'_jc_save_fromDate', 'value':time})
                      
                      driver.find_element_by_id('query_ticket').submit()
                      sleep(2)
                      fromStation = driver.find_element_by_id('fromStationText').click()
                      driver.find_element_by_id('fromStationText').send_keys(from_station)
                      driver.find_element_by_id('fromStationText').send_keys(Keys.ENTER)
                      sleep(3)
                      toStation   = driver.find_element_by_id('toStationText').click()
                      driver.find_element_by_id('toStationText').send_keys(to_station)
                      driver.find_element_by_id('toStationText').send_keys(Keys.ENTER)                      
                      sleep(2)
                      
                      count = 0                     
                      while driver.current_url[0:41] == ticket_url:
                                 driver.find_element_by_id('query_ticket').click()
                                 #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_id('t-list').is_displayed())
                                 sleep(5)
                                 count +=1
                                 print "循环点击查询... 第 %s 次" % count
                                 sleep(1)
                                 try:
                                            driver.find_element_by_link_text("预订").click()
                                            sleep(1)
                                 except:
                                            print "还没开始预订"
                                            continue                    
                      
           except Exception as e:
                      print e
if __name__ == "__main__":
           
           #格式：qiangpiao('123456','1123456',u'南京',u'上海','2016-01-01')
           qiangpiao(username,password,from_station,to_station,time)




