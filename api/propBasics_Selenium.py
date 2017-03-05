from datetime import datetime
import re

def getPropBasics_Selenium(element, leaseObj):
    price = getPrice(element)
    bedrooms = getBedrooms(element)
    leaseObj['posted_at'] = getDate(element)
    leaseObj['whole_price'] = price
    leaseObj['address'] = getAddressString(element)
    leaseObj['company'] = getLandlord(element)
    leaseObj['rooms'] = [{
            'room_type': getPricePerRoom(price, bedrooms),
            'reg_price': 0,
    		'rooms_per': bedrooms,
    		'lease_terms': 0,
    		'bathrooms': getBathrooms(element)
        }]
    leaseObj['furnished']: getFurnished(element)
    return leaseObj

def getDate(element):
    date = element[0].find_element_by_xpath("//*[@id='itemdetails']/div[2]/table/tbody/tr[1]/td").get_attribute('innerHTML')
    datetime_unix = datetime.strptime(date, '%d-%b-%y').strftime('%s')
    return datetime_unix

def getPrice(element):
    price = element[1].find_element_by_xpath("//*[@id='itemdetails']/div[2]/table/tbody/tr[2]/td/div/span/strong").get_attribute('innerHTML')
    splitPrice = price.split('.')[0]
    formattedPrice = splitPrice.replace("$", "").replace(",", "")
    intPrice = int(formattedPrice)
    return intPrice

def getAddressString(element):
    addressString = element[2].find_element_by_xpath("//*[@id='itemdetails']/div[2]/table/tbody/tr[3]/td").get_attribute('innerHTML')
    splitAddress = addressString.split('<br>')[0]
    return splitAddress

def getBedrooms(element):
    bedrooms = element[4].find_element_by_xpath("//*[@id='itemdetails']/div[2]/table/tbody/tr[5]/td").get_attribute('innerHTML')
    # Python Regex https://www.tutorialspoint.com/python/python_reg_expressions.htm
    matched_bedrooms = re.search(r'\d', bedrooms).group()
    intBedrooms = int(matched_bedrooms)
    return intBedrooms

def getBathrooms(element):
    bathrooms = element[5].find_element_by_xpath("//*[@id='itemdetails']/div[2]/table/tbody/tr[6]/td").get_attribute('innerHTML')
    matched_bathrooms = re.search(r'\d', bathrooms).group()
    intBathrooms = int(matched_bathrooms)
    return intBathrooms

def getLandlord(element):
    landlord = element[5].find_element_by_xpath("//*[@id="itemdetails"]/div[2]/table/tbody/tr[8]/td").get_attribute('innerHTML')
    return landlord


def getPricePerRoom(price, bedrooms):
    perRoom = price/bedrooms
    return perRoom
