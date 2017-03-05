from selenium.common.exceptions import TimeoutException, ElementNotVisibleException

from api.propBasics_Selenium import getPropBasics_Selenium
from api.propBasics_NLP import getPropBasics_NLP
from api.demographics import getDemographics
from api.images import extractImages
from api.propBasics_GPS import getPropBasics_GPS

page = {}
googleAPI = {}

# takes 2 args, a driver instance and a query string
def beginScript(driver, url, city, property_type):
    driver.get(url)
    try:
        statsTable = driver.find_elements_by_xpath("//table[@class='ad-attributes']/tbody/tr")
        paragraph = driver.find_element_by_xpath("//*[@id='UserContent']/table/tbody/tr/td/span")

        leaseObj = {}
        leaseObj = getPropBasics_Selenium(statsTable, leaseObj)
        leaseObj = getPropBasics_NLP(paragraph, leaseObj)
        leaseObj = getDemographics(paragraph, leaseObj)
        leaseObj = extractImages(page, leaseObj)
        leaseObj = getPropBasics_GPS(googleAPI, leaseObj)

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
