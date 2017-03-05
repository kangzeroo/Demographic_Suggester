import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException

from api.functions import getTableAttrs
from api.nlp import getUtilsAttrs

# creates the driver instance
def init_driver():
    driver = webdriver.Firefox()
    # adds the WebDriverWait as an attribute, which makes it wait 5 seconds for an event to occur
    driver.wait = WebDriverWait(driver, 5)
    return driver

# takes 2 args, a driver instance and a query string
def getPropertyDetails(driver, url, city, property_type):
    driver.get(url)
    try:
        tbody = driver.find_elements_by_xpath("//table[@class='ad-attributes']/tbody/tr")
        paragraph = driver.find_element_by_xpath("//*[@id='UserContent']/table/tbody/tr/td/span")
        leaseObj = {}
        leaseObj = getTableAttrs(tbody, leaseObj)
        leaseObj = getUtilsAttrs(paragraph, leaseObj)
        leaseObj['city'] = city
        leaseObj['company'] = "Private Landlord"
        leaseObj['type'] = 'property_type'
        leaseObj['active'] = True
        leaseObj['claimed'] = False
        leaseObj['deleted'] = False
        leaseObj['thumbnail'] = 'https://s3.amazonaws.com/rentburrow-images/ideas%2540bytenectar.io/default_home_icon.png'
        leaseObj['note'] = paragraph
        print(leaseObj)
    except TimeoutException:
        print('TimeoutException')


# __name__ is the python running script. if this file is run directly, then __name__ == "__main__"
# if we imported this script, then __name__ != __main__
if __name__ == "__main__":
    driver = init_driver()
    url = "http://www.kijiji.ca/v-house-rental/kitchener-waterloo/waterloo-townhome-for-rent-laurelwood/1241107253"
    getPropertyDetails(driver, url, 'Toronto', 'house')
    time.sleep(5)
    driver.quit()
