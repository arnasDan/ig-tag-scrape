import time
import random
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def login(username, password, driver):
    driver.get('https://www.instagram.com/accounts/login/')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'input')))
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
    time.sleep(5 * random.random())
    driver.find_element_by_xpath("//button[contains(text(),'Log in')]").click()
    time.sleep(5 * random.random())
    
def scrape_once(driver, tagDict):
    tagCount = 0
    postCount = 0
    driver.get('https://www.instagram.com/explore')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'article')))   
    all_links = driver.find_elements_by_tag_name('a')
    for link in all_links:
        href = link.get_attribute('href')
        if (href.endswith('?explore=true')):
            media_html = requests.get(href).text
            soup = BeautifulSoup(media_html, 'lxml')
            hashtags = soup.findAll(attrs={"property" : "instapp:hashtags"})
            for tagElement in hashtags:
                tag = tagElement.get('content')
                tagDict[tag] += 1
                tagCount += 1               
            postCount += 1
    print('%d tags processed in %d posts' % (tagCount, postCount))