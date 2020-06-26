  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:/Users/Solomon/chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
time.sleep(15)
msg = " "
username = 'name'  //the name of your contact to whom you want to send  
string = 'Hey this is Solo-bot, this text is automatically sent to you. If received call solomon and let him know ' \
         'that you received this text '
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(username))
user.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div'
#inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(1):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)
