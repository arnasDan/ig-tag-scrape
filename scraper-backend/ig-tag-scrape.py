import os
import sys
import operator
from scraper import login
from scraper import scrape_once
from collections import defaultdict
from selenium import webdriver

os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.abspath(__file__)) + r'\node_modules\geckodriver'

def read_login(filename: str):
    username: str
    password: str
    with open(filename,'r') as f:
        username = f.readline()
        password = f.readline()
    return (username, password)

print('Inicialising scraper...')
options = webdriver.FirefoxOptions()
#options.headless = True #broken if headless :/
driver = webdriver.Firefox(options=options)
    
loginData = read_login(sys.argv[1])
login(loginData[0], loginData[1], driver)
tagDict = defaultdict(int)
print('Scraping data...')
for i in range(3):
    print('Pass no. %d' % (i + 1))
    scrape_once(driver, tagDict)

for tag in sorted(tagDict.items(), key=operator.itemgetter(1), reverse=True):
    print(tag[0] + ' ' + str(tag[1]))
driver.quit()
