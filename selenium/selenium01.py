from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'/home/abondr/Documents/web_drivers/chromedriver')
driver.get("https://ebemoney.club/")
time.sleep(1)
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys("abondr")
password.send_keys("Abondr@1984")
driver.execute_script('dologin()')
"""after login"""
time.sleep(1)
driver.execute_script('doarea(2)')
"""after gone to captcha area,wait for captcha to load"""

for times in range(0,99999):
    # time.sleep(1)
    captchaText = ""
    if(times % 100 == 0):
        print("present line ",times)
    for index in range(1,4):
        imgSrc = driver.find_element_by_xpath("//div[@id='cimg"+str(index)+"']/img[1]").get_attribute("src")
        captchaText += imgSrc[-5]
    driver.find_element_by_name("capcha").send_keys(captchaText)
    driver.execute_script('dosub()')





