import os
import sys
import operator
import logging
from scraper import login
from scraper import scrape_once
from collections import defaultdict
from selenium import webdriver
from argparse import ArgumentParser

os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.abspath(__file__)) + r'\node_modules\geckodriver'

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename", default='login.txt',
                    help="Login file name (default: login.txt)", metavar="FILE")
parser.add_argument("-q", "--quiet", dest="quiet", action="store_true",
                    help="Don't print to console")
parser.add_argument("-c", "--collect", dest="collect_dict", action="store_true",
                    help="Collect tags into one large dict.")
parser.add_argument("-p", "--pass_count", dest="passes", default=1, type=int,
                    help="Number of passes to perform (default: 1)", metavar="NO_OF_PASSES")

args = parser.parse_args()
print = logging.info
logging.basicConfig(level=logging.WARNING if args.quiet else logging.INFO,
                    format="%(message)s")

def read_login(filename: str):
    username: str
    password: str
    with open(filename,'r') as f:
        username = f.readline()
        password = f.readline()
    return (username, password)

print('Inicialising scraper...')
options = webdriver.FirefoxOptions()
options.headless = args.quiet
driver = webdriver.Firefox(options=options)
    
loginData = read_login(args.filename)
login(loginData[0], loginData[1], driver)
tagDict = defaultdict(int)
print('Scraping data...')
for i in range(args.passes):
    print('Pass no. %d' % (i + 1))
    scrape_once(driver, args.collect_dict, tagDict)

for tag in sorted(tagDict.items(), key=operator.itemgetter(1), reverse=True):
    print(tag[0] + ' ' + str(tag[1]))
driver.quit()
