import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from api.script_order import beginScript


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
    url = "http://www.kijiji.ca/v-house-rental/kitchener-waterloo/waterloo-townhome-for-rent-laurelwood/1241107253"
    beginScript(driver, url, 'Toronto', 'house')
    time.sleep(5)
    driver.quit()
