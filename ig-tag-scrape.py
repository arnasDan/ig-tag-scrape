from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
from scraper import login
from scraper import scrape_once
from collections import defaultdict

os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.abspath(__file__)) + r'\node_modules\geckodriver'

print('Inicialising scraper...')
options = webdriver.FirefoxOptions()
#options.headless = True #broken if headless :/
driver = webdriver.Firefox(options=options)
username: str
password: str
with open('login.txt','r') as f:
    username = f.readline()
    password = f.readline()
login(username, password, driver)
tagDict = defaultdict(int)
print('Scraping data...')
for i in range(1):
    print('Pass no. %d' % (i + 1))
    scrape_once(driver, tagDict)

for tag in tagDict.items():
    print(tag[0] + ' ' + str(tag[1]))
driver.quit()
