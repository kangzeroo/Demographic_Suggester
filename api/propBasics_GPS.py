def getPropBasics_GPS(googleAPI, leaseObj):
    return leaseObj


def getGPSCoords(googleAPI, leaseObj):
    leaseObj['core']['coords'] = [-45.453445, 80.893457]
    return leaseObj

def getPlaceId(googleAPI, leaseObj):
    leaseObj['core']['place_id'] = 'DLJF034FD9'
    return leaseObj
