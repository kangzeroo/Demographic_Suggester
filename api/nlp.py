import re

def getUtilsAttrs(paragraph, leaseObj):
    leaseObj['utils_list'] = {}
    leaseObj = getUtils(paragraph, leaseObj)

def getUtils(paragraph, leaseObj):
    hydro_and_internet_incl = re.search(r'', paragraph, re.I).group() # hydro and internet included
    utils_incl_except_hydro = re.search(r'', paragraph, re.I).group() # utilities included, except hydro
    amenities = re.search(r'', paragraph, re.I).group() # amenities
    all_utils = re.search(r'', paragraph, re.I).group() # all utilities
    all_incl = re.search(r'', paragraph, re.I).group() # all inclusive
    comma_incl = re.search(r'', paragraph, re.I).group() # water, electric, internet included
    plus_utils = re.search(r'(plus utilities)|(plus utils)', paragraph, re.I).group()   # plus utilities
    utils_incl = re.search(r'(utilities incl)|(utils incl)', paragraph, re.I).group()   # utilities included

    # broad-first search

    # leaseObj['utils_list']['water'] = True
    # leaseObj['utils_list']['heat'] = True
    # leaseObj['utils_list']['electric'] = True
    # leaseObj['utils_list']['internet'] = True

    return leaseObj

def getWater(paragraph, leaseObj):
    if leaseObj['utils_list']['water'] == True:
        water_extra = re.search(r'', paragraph, re.I).group() # water extra, not included
        return leaseObj
    else:
        water_incl = re.search(r'', paragraph, re.I).group() # water incl
        return leaseObj

def getHeat(paragraph, leaseObj):
    if leaseObj['utils_list']['heat'] == True:
        heat_extra = re.search(r'', paragraph, re.I).group()    # heat extra, heating not incl
        gas_extra = re.search(r'', paragraph, re.I).group()     # gas extra, gas not incl
        return leaseObj
    else:
        gas_incl = re.search(r'', paragraph, re.I).group()   # gas incl
        heating_incl = re.search(r'', paragraph, re.I).group()   # heating incl
        return leaseObj

def getElectric(paragraph, leaseObj):
    if leaseObj['utils_list']['electric'] == True:
        hydro_extra = re.search(r'', paragraph, re.I).group() # hydro extra, not included
        electric_extra = re.search(r'', paragraph, re.I).group() # electricity, electric not included
        return leaseObj
    else:
        elec_incl = re.search(r'', paragraph, re.I).group() # electric incl
        power_incl = re.search(r'', paragraph, re.I).group()    # power incl
        return leaseObj

def getFurnished(paragraph, leaseObj):
    fully_furn = re.search(r'', paragraph, re.I).group()   # fully furnished
    furn_incl = re.search(r'', paragraph, re.I).group()   # furniture included
    return leaseObj

def getParking(paragraph, leaseObj):
    parking_extra = re.search(r'', paragraph, re.I).group()   # parking extra
    parking_avail = re.search(r'', paragraph, re.I).group() # parking available
    return leaseObj

def getFreeParking(paragraph, leaseObj):
    free_parking = re.search(r'', paragraph, re.I).group()   # free parking, parking free
    return leaseObj

def getInternet(paragraph, leaseObj):
    unlim_wifi = re.search(r'', paragraph, re.I).group()   # unlimited wifi
    high_speed_int = re.search(r'', paragraph, re.I).group()   # high speed internet
    unlim_int = re.search(r'', paragraph, re.I).group()   # unlimited internet
    int_extra = re.search(r'', paragraph, re.I).group()   # internet extra
    free_int = re.search(r'', paragraph, re.I).group()   # free internet
    return leaseObj


def getAc(paragraph, leaseObj):
    air_cond = re.search(r'', paragraph, re.I).group()   # air-conditioned, air conditioning
    AC = re.search(r'', paragraph, re.I).group() # A/C, AC
    return leaseObj

def getGym(paragraph, leaseObj):
    gym = re.search(r'', paragraph, re.I).group() # gym
    fitness_room = re.search(r'', paragraph, re.I).group() # fitness room
    return leaseObj

def getLaundry(paragraph, leaseObj):
    # laundry
    # coin laundry
    # laundry onsite
    return leaseObj

def getRoomInfo(paragraph, leaseObj):
    # spacious rooms
    # cozy rooms
    # big rooms, large rooms
    return leaseObj



# utils_list: {
# 		id: String,
# 		water: Boolean,
# 		heat: Boolean,
# 		electric: Boolean,
# 		furnished: Boolean,
# 		parking: Boolean,
# 		free_parking: Boolean,
# 		internet: Boolean,
# 		ac: Boolean,
# 		laundry: Boolean
# 	},
