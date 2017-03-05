import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from api.pagination import beginScript


# creates the driver instance
def init_driver():
    driver = webdriver.Firefox()
    # adds the WebDriverWait as an attribute, which makes it wait 5 seconds for an event to occur
    driver.wait = WebDriverWait(driver, 5)
    return driver


# __name__ is the python running script. if this file is run directly, then __name__ == "__main__"
# if we imported this script, then __name__ != __main__
if __name__ == "__main__":
    driver = init_driver()
    urls = [
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/danforth-woodbine-entire-detached-house-for-rent/1243834480',
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/3-bedroom-townhouse-in-the-junction/1244219311?enableSearchNavigationFlag=true',
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/newly-renovated-3-br-home-in-queen-west-main-second-floor/1244200671?enableSearchNavigationFlag=true',
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/2-bedrooms-townhouse-for-rent-toronto/1244180860?enableSearchNavigationFlag=true',
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/house-near-kennedy-subway-station/1244203290?enableSearchNavigationFlag=true',
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/beautiful-2-br-2wr-1pk-condo-facing-south-east/1242258625',
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/brand-new-3-bedroom-townhouse-yonge-eglinton/1222567315?enableSearchNavigationFlag=true'
    ]
    for url in urls:
        beginScript(driver, url, 'Toronto', 'house')
    time.sleep(5)
    driver.quit()
