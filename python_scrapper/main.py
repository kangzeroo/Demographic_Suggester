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
    # urls = [
    #     'http://www.kijiji.ca/v-house-rental/city-of-toronto/danforth-woodbine-entire-detached-house-for-rent/1243834480',
    #     'http://www.kijiji.ca/v-house-rental/city-of-toronto/3-bedroom-townhouse-in-the-junction/1244219311?enableSearchNavigationFlag=true',
    #     'http://www.kijiji.ca/v-house-rental/city-of-toronto/newly-renovated-3-br-home-in-queen-west-main-second-floor/1244200671?enableSearchNavigationFlag=true'
    # ]
    urls = [
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/2-bedrooms-townhouse-for-rent-toronto/1244180860?enableSearchNavigationFlag=true',
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/house-near-kennedy-subway-station/1244203290?enableSearchNavigationFlag=true',
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/beautiful-2-br-2wr-1pk-condo-facing-south-east/1242258625',
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/brand-new-3-bedroom-townhouse-yonge-eglinton/1222567315?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-room-rental-roommate/city-of-toronto/master-bedroom-750-month-don-mills-sheppard-wifi/1244244700?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-house-for-sale/mississauga-peel-region/dream-home-for-first-time-home-buyers-semi-detached/1244238544'
        'http://www.kijiji.ca/v-1-bedroom-apartments-condos/city-of-toronto/1-bdm-coach-house-for-rent-in-the-leaside-neighbourhood/1185376253'
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/4-bedroom-2-bathroom-house-for-rent-in-etobicoke/1244222135?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-room-rental-roommate/city-of-toronto/875newly-renovated-house-at-downtown-area-875-month/1244217824?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-house-rental/oshawa-durham-region/gergeous-4-bedroom-house-for-rent-in-taunton-harmony-oshawa/1243591494?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-house-rental/st-catharines/4-or-5-rooms-available-all-inclusive-very-close-to-university/1244215874?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-3-bedroom-apartments-condos/city-of-toronto/newly-renovated-3-bedroom-town-houses-40-godstone-road/1224955331'
        'http://www.kijiji.ca/v-room-rental-roommate/city-of-toronto/2-bedroom-wonderful-large-basement-apartment-in-a-house/1244213723?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-room-rental-roommate/city-of-toronto/beautiful-3-bedroom-upstairs-only-house-1800-north-york/1244212824?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-room-rental-roommate/city-of-toronto/beautiful-3-bedroom-upstairs-only-house-1800-north-york/1244212824?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-house-rental/markham-york-region/detached-house-3-bedrooms-2-wr-in-danforth/1244211733?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-house-for-sale/mississauga-peel-region/open-house-today-3-br-detached-with-apt-lisgar-mississauga/1244209606?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/danforth-woodbine-entire-detached-house-for-rent/1243834480'
        'http://www.kijiji.ca/v-house-for-sale/mississauga-peel-region/open-house-today-3-br-detached-with-apt-lisgar-mississauga/1244209606?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-3-bedroom-apartments-condos/city-of-toronto/765-steeles-three-bedroom-apartment-for-rent/1134228596'
        'http://www.kijiji.ca/v-house-rental/city-of-toronto/house-near-kennedy-subway-station/1244203290?enableSearchNavigationFlag=true'
        'http://www.kijiji.ca/v-short-term-rental/city-of-toronto/house-for-rent-norseman-height-sunnylea/1244187040?enableSearchNavigationFlag=true'
    ]
    for url in urls:
        beginScript(driver, url, 'Toronto', 'house')
    time.sleep(5)
    driver.quit()
