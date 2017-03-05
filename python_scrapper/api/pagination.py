from api.buildLease import buildLeaseObj

def beginScript(driver, url, city, property_type):
    buildLeaseObj(driver, url, city, property_type)
