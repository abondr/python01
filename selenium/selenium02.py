from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
ua = UserAgent()
userAgent = ua.
print(userAgent)
options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\ChromeDriver\chromedriver_win32\chromedriver.exe')
driver.get("http://theinstantjob.com/login.php")

username = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")
username.send_keys("abondr.job@gmail.com")
password.send_keys("Abondr@1984")
regBtn = driver.find_element_by_class_name("registerbtn")
regBtn.click()
