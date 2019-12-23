from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Chrome(r'/home/abondr/Documents/web_drivers/chromedriver')
time.sleep(1)
for i in range(1, 47):
    driver.get("http://www.ebaystores.com/SwordNArmory/Home.html_?rt=nc&_sid=795588326&_trksid=p4634.c0.m352.l1581&_pgn="+str(i))
    tds = driver.find_elements_by_css_selector('.gallery')
    for td in tds:
      time.sleep(1)
      row = []
      ahrf = td.find_element_by_tag_name("a")
      imgs1 = td.find_elements_by_css_selector(".image img[itemprop='image']")
      if ahrf.get_attribute('href') is None:
          continue
      row.append(ahrf.get_attribute('href'))
      for img in imgs1:
        row.append(img.get_attribute("alt"))
        row.append(img.get_attribute("src"))
      spanPrice = td.find_elements_by_css_selector("span[itemprop='price']")
      for price in spanPrice:
          row.append(price.text)
      with open('products.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
      csvFile.close()