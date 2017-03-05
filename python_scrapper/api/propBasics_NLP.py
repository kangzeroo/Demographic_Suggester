import re

def getPropBasics_NLP(paragraph, leaseObj):
    leaseObj = getUtils(paragraph, leaseObj)
    leaseObj = getWater(paragraph, leaseObj)
    leaseObj = getHeat(paragraph, leaseObj)
    leaseObj = getElectric(paragraph, leaseObj)
    leaseObj = getFurnished(paragraph, leaseObj)
    leaseObj = getParking(paragraph, leaseObj)
    leaseObj = getFreeParking(paragraph, leaseObj)
    leaseObj = getInternet(paragraph, leaseObj)
    leaseObj = getAc(paragraph, leaseObj)
    leaseObj = getGym(paragraph, leaseObj)
    leaseObj = getLaundry(paragraph, leaseObj)
    leaseObj = getFurnished(paragraph, leaseObj)
    leaseObj = getRoomInfo(paragraph, leaseObj)
    return leaseObj

def setAllUtils(leaseObj):
    # broad-first search
    leaseObj['utils_list']['water'] = True
    leaseObj['utils_list']['heat'] = True
    leaseObj['utils_list']['electric'] = True
    leaseObj['utils_list']['internet'] = True
    return leaseObj

# catch-all utilities incl
# in order of broad-search first
def getUtils(paragraph, leaseObj):

    # amenities
    try:
        hydro_and_internet_incl = re.search(r'(amenities incl)|(amenities included)|(all amenities)', paragraph, re.I).group()
        print(hydro_and_internet_incl)
        leaseObj = setAllUtils(leaseObj)
    except:
        print('NOT FOUND ==> # amenities')
        pass

    # all utilities
    try:
        all_utilities = re.search(r'(all utilities)|(all utils)|(utilities included)|(utilities incl)|(utils incl)|(utils included)', paragraph, re.I).group()
        print(all_utilities)
        leaseObj = setAllUtils(leaseObj)
    except:
        print('NOT FOUND ==> # all utilities')
        pass

    # all inclusive
    try:
        all_inclusive = re.search(r'(all inclusive)|(all included)|(everything included)', paragraph, re.I).group()
        print(hydro_and_internet_incl)
        leaseObj = setAllUtils(leaseObj)
        leaseOjb['utils_list']['furniture'] = True
    except:
        print('NOT FOUND ==> # all inclusive')
        pass

    # plus utilities
    try:
        hydro_and_internet_incl = re.search(r'(hydro and internet included)|(hydro and internet incl)|(includes hydro and internet)', paragraph, re.I).group()
        print(hydro_and_internet_incl)
        leaseObj = setAllUtils(leaseObj)
    except:
        print('NOT FOUND ==> # plus utilities')
        pass

    # utilities included
    try:
        hydro_and_internet_incl = re.search(r'(hydro and internet included)|(hydro and internet incl)|(includes hydro and internet)', paragraph, re.I).group()
        print(hydro_and_internet_incl)
        leaseObj = setAllUtils(leaseObj)
    except:
        print('NOT FOUND ==> # utilities included')
        pass

    # water, electric, internet included
    try:
        hydro_and_internet_incl = re.search(r'(hydro and internet included)|(hydro and internet incl)|(includes hydro and internet)', paragraph, re.I).group()
        print(hydro_and_internet_incl)
        leaseObj = setAllUtils(leaseObj)
    except:
        print('NOT FOUND ==> # water, electric, internet included')
        pass

    print("------------ next regex ------------")
    return leaseObj

def getWater(paragraph, leaseObj):
   if leaseObj['utils_list']['water'] == True:
        # water extra, not included
        try:
            water_extra = re.search(r'(water extra, not included)|(water not included)', paragraph, re.I).group() # water extra, not included
            print(water_extra)
        except:
            print("NOT FOUND ==> # water extra, not include")
            pass
        return leaseObj
    else:
        try:
            water_incl = re.search(r'(water included)', paragraph, re.I).group() # water incl
            print(water_incl)
        except:
            print ("NOT FOUND ==> water included")
        return leaseObj

def getHeat(paragraph, leaseObj):
    if leaseObj['utils_list']['heat'] == True:
        # heat extra, heating not incl
        try:
            heat_extra = re.search(r'(heat extra, not included)|(heat not included)', paragraph, re.I).group()
            print(heat_extra)
        except:
            print("NOT FOUND ==> # heat extra, not included")
        # gas extra, gas not incl
        try:
            gas_extra = re.search(r'(gas extra, not included)|(gas not included)', paragraph, re.I).group()
        return leaseObj
    else:
        # gas incl
        try:
            gas_incl = re.search(r'(gas included)', paragraph, re.I).group()
        except:
            print("NOT FOUND ==> # gas included")
        # heating incl
        try:
            heating_incl = re.search(r'(heating included)', paragraph, re.I).group()
        except:
            print("NOT FOUND ==> # heat included")
        return leaseObj

def getElectric(paragraph, leaseObj):
    if leaseObj['utils_list']['electric'] == True:
        # hydro extra, not included
        try:
            hydro_extra = re.search(r'(hydro is extra, not included)| (extra hydro, not included)', paragraph, re.I).group()
        except:
            print("NOT FOUND ==> # extra hydro")
        # electricity, electric not included
        try:
            electric_extra = re.search(r'(electric is extra, not included)|(extra electrical, not included)', paragraph, re.I).group()
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

def getFurnished(element, leaseObj):
    furnished = element[8].find_element_by_xpath("//*[@id='itemdetails']/div[2]/table/tbody/tr[9]/td").get_attribute('innerHTML')
    matched_furnished = re.search(r'No|Yes', furnished).group()
    print(matched_furnished)
    if matched_furnished == 'Yes':
        return True
    else:
        return False

def getRoomInfo(paragraph, leaseObj):
    # spacious rooms
    # cozy rooms
    # big rooms, large rooms
    leaseObj['rooms']['room_desciptions'] = []
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
