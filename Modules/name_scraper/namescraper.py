
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "/Users/rai0x00/Desktop/projects/kitsune/modules/name_scraper/chromedriver"


def search(name, add):
    driver = webdriver.Chrome(PATH)
    driver.get("https://thatsthem.com")

    search = driver.find_element_by_id("fullName")
    search.send_keys(name, Keys.RETURN)

    search = driver.find_element_by_id("address")
    search.send_keys(add, Keys.RETURN)
    driver.quit()

    driver.get("https://www.fastpeoplesearch.com")    

    search = driver.find_element_by_id("search-name-name")
    search.send_keys(name, Keys.RETURN)

    search = driver.find_element_by_id("search-name-address")
    search.send_keys(add, Keys.RETURN)
    driver.quit()

    driver.get("https://www.truepeoplesearch.com")    

    search = driver.find_element_by_id("id-d-n")
    search.send_keys(name, Keys.RETURN)

    search = driver.find_element_by_id("id")
    search.send_keys(add, Keys.RETURN)
    driver.quit() 