
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def thatthem_search(name, add):
    PATH = "/Users/rai0x00/Desktop/projects/kitsune/modules/name_scraper/chromedriver"
    driver = webdriver.Chrome(PATH)

    driver.get("https://thatsthem.com")

    search = driver.find_element_by_id("fullName")
    search.send_keys(name, Keys.RETURN)

    search = driver.find_element_by_id("address")
    search.send_keys(add, Keys.RETURN)
    driver.quit()


