
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
import time

PATH = "/Users/rai0x00/Desktop/projects/kitsune/modules/name_scraper/chromedriver"


def search(name):
    driver = webdriver.Chrome(PATH)
    driver.get("https://thatsthem.com")

    search = driver.find_element_by_id("fullName")
    search.send_keys(name, Keys.RETURN)
    res1 = driver.find_element_by_class_name("ThatsThem-record")
    print(res1.text)

    driver.get("https://www.fastpeoplesearch.com")    
    search = driver.find_element_by_id("search-name-name")
    search.send_keys(name, Keys.RETURN)
    res2 = driver.find_element_by_class_name("card")
    print(res2.text)

    driver.get("https://www.truepeoplesearch.com")    
    search = driver.find_element_by_id("id-d-n")
    search.send_keys(name, Keys.RETURN)
    details = driver.find_element_by_link_text("View Details") 
    details.click()
    res3 = driver.find_element_by_class_name("col")
    print(res3.text)
    
    driver.quit()
    