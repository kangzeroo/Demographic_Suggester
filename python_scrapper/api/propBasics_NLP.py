import re

def getPropBasics_NLP(paragraph, leaseObj):
    # leaseObj = getUtils(paragraph, leaseObj)
    # leaseObj = getWater(paragraph, leaseObj)
    # leaseObj = getHeat(paragraph, leaseObj)
    # leaseObj = getElectric(paragraph, leaseObj)
    # leaseObj = getFurnished(paragraph, leaseObj)
    # leaseObj = getParking(paragraph, leaseObj)
    # leaseObj = getFreeParking(paragraph, leaseObj)
    # leaseObj = getInternet(paragraph, leaseObj)
    # leaseObj = getAc(paragraph, leaseObj)
    # leaseObj = getGym(paragraph, leaseObj)
    # leaseObj = getLaundry(paragraph, leaseObj)
    # leaseObj = getFurnished(paragraph, leaseObj)
    # leaseObj = getRoomInfo(paragraph, leaseObj)
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
# def getUtils(paragraph, leaseObj):
#
#     # amenities
#     try:
#         hydro_and_internet_incl = re.search(r'(amenities incl)|(amenities included)|(all amenities)', paragraph, re.I).group()
#         print(hydro_and_internet_incl)
#         leaseObj = setAllUtils(leaseObj)
#     except:
#         print('NOT FOUND ==> # amenities')
#         pass
#
#     # all utilities
#     try:
#         all_utilities = re.search(r'(all utilities)|(all utils)|(utilities included)|(utilities incl)|(utils incl)|(utils included)', paragraph, re.I).group()
#         print(all_utilities)
#         leaseObj = setAllUtils(leaseObj)
#     except:
#         print('NOT FOUND ==> # all utilities')
#         pass
#
#     # all inclusive
#     try:
#         all_inclusive = re.search(r'(all inclusive)|(all included)|(everything included)', paragraph, re.I).group()
#         print(hydro_and_internet_incl)
#         leaseObj = setAllUtils(leaseObj)
#         leaseOjb['utils_list']['furniture'] = True
#     except:
#         print('NOT FOUND ==> # all inclusive')
#         pass
#
#     # plus utilities
#     try:
#         hydro_and_internet_incl = re.search(r'(hydro and internet included)|(hydro and internet incl)|(includes hydro and internet)', paragraph, re.I).group()
#         print(hydro_and_internet_incl)
#         leaseObj = setAllUtils(leaseObj)
#     except:
#         print('NOT FOUND ==> # plus utilities')
#         pass
#
#     # utilities included
#     try:
#         hydro_and_internet_incl = re.search(r'(hydro and internet included)|(hydro and internet incl)|(includes hydro and internet)', paragraph, re.I).group()
#         print(hydro_and_internet_incl)
#         leaseObj = setAllUtils(leaseObj)
#     except:
#         print('NOT FOUND ==> # utilities included')
#         pass
#
#     # water, electric, internet included
#     try:
#         hydro_and_internet_incl = re.search(r'(hydro and internet included)|(hydro and internet incl)|(includes hydro and internet)', paragraph, re.I).group()
#         print(hydro_and_internet_incl)
#         leaseObj = setAllUtils(leaseObj)
#     except:
#         print('NOT FOUND ==> # water, electric, internet included')
#         pass
#
#     print("------------ next regex ------------")
#     return leaseObj
#
# def getWater(paragraph, leaseObj):
#    if leaseObj['utils_list']['water'] == True:
#         # water extra, not included
#         try:
#             water_extra = re.search(r'(water extra, not included)|(water not included)', paragraph, re.I).group() # water extra, not included
#             print(water_extra)
#         except:
#             print("NOT FOUND ==> # water extra, not include")
#             pass
#     else:
#         try:
#             water_incl = re.search(r'(water included)', paragraph, re.I).group() # water incl
#             print(water_incl)
#         except:
#             print ("NOT FOUND ==> water included")
#     return leaseObj
#
# def getHeat(paragraph, leaseObj):
#     if leaseObj['utils_list']['heat'] == True:
#         # heat extra, heating not incl
#         try:
#             heat_extra = re.search(r'(heat extra, not included)|(heat not included)', paragraph, re.I).group()
#             print(heat_extra)
#         except:
#             print("NOT FOUND ==> # heat extra, not included")
#         # gas extra, gas not incl
#         try:
#             gas_extra = re.search(r'(gas extra, not included)|(gas not included)', paragraph, re.I).group()
#     else:
#         # gas incl
#         try:
#             gas_incl = re.search(r'(gas included)', paragraph, re.I).group()
#         except:
#             print("NOT FOUND ==> # gas included")
#         # heating incl
#         try:
#             heating_incl = re.search(r'(heating included)', paragraph, re.I).group()
#         except:
#             print("NOT FOUND ==> # heat included")
#     return leaseObj
#
# def getElectric(paragraph, leaseObj):
#     if leaseObj['utils_list']['electric'] == True:
#         # hydro extra, not included
#         try:
#             hydro_extra = re.search(r'(hydro is extra, not included)| (extra hydro, not included)', paragraph, re.I).group()
#         except:
#             print("NOT FOUND ==> # extra hydro")
#         # electricity, electric not included
#         try:
#             electric_extra = re.search(r'(electric is extra, not included)|(extra electrical, not included)', paragraph, re.I).group()
#         except:
#             print("NOT FOUND ==> # extra electrical")
#     else:
#         # electric incl
#         try:
#             elec_incl = re.search(r'(electrical included)|(included electrical)', paragraph, re.I).group()
#         except:
#             print("NOT FOUND ==> # electrical included")
#         # power incl
#         try:
#             power_incl = re.search(r'(power included)|(included power)', paragraph, re.I).group()
#         except:
#             print("NOT FOUND ==> # power included")
#     return leaseObj
#
# def getFurnished(paragraph, leaseObj):
#     # fully furnished
#     try:
#         fully_furn = re.search(r'(fully furnished)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # fully furnished")
#     # furniture included
#     try:
#         furn_incl = re.search(r'(furniture included)|(included furnature)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # furniture included")
#     return leaseObj
#
# def getParking(paragraph, leaseObj):
#     # parking extra
#     try:
#         parking_extra = re.search(r'(extra parking)|(parking is extra)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # extra parking")
#     # parking available
#     try:
#         parking_avail = re.search(r'(available parking)|(parking is available)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # available parking")
#     return leaseObj
#
# def getFreeParking(paragraph, leaseObj):
#     # free parking, parking free
#     try:
#         free_parking = re.search(r'(free parking)|(parking is free)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # free parking")
#     return leaseObj
#
# def getInternet(paragraph, leaseObj):
#     # unlimited wifi
#     try:
#         unlim_wifi = re.search(r'(unlimited wifi)|(wifi is unlimited)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # unlimited wifi")
#     # high speed internet
#     try:
#         high_speed_int = re.search(r'(high speed internet included)|(includes high speed internet)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # high speed internet")
#     # unlimited internet
#     try:
#         unlim_int = re.search(r'(unlimited internet provided)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # unlimited internet provided")
#     # internet extra
#     try:
#         int_extra = re.search(r'(internet is extra)|(extra internet)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # internet is extra")
#     # free internet
#     try:
#         free_int = re.search(r'(Free Internet)|(internet is free)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # free internet")
#     return leaseObj
#
#
# def getAc(paragraph, leaseObj):
#     # air-conditioned, air conditioning
#     try:
#         air_cond = re.search(r'(air conditioning is provided)|(provided with air conditioning)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # provided air conditioning")
#     # A/C, AC
#     try:
#         AC = re.search(r'(air conditioning is NOT provided)|(AC Not provided)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # air conditioning")
#     return leaseObj
#
# def getGym(paragraph, leaseObj):
#     # gym
#     try:
#         gym = re.search(r'(gym is provided)|(access to gym)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # gym provided")
#     # fitness room
#     try:
#         fitness_room = re.search(r'(fitness room is provided)|(access to a fitness room)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> # fitness room")
#     return leaseObj
#
# def getLaundry(paragraph, leaseObj):
#     # laundry
#     # coin laundry
#     # laundry onsite
#     try:
#         laundry = re.search(r'(laundry machine provided)|(avialble laundry machine)', paragraph, re.I).group()
#     except:
#         print("NOT FOUND ==> laundry")
#     return leaseObj

# def getFurnished(element, leaseObj):
#     furnished = element[8].find_element_by_xpath("//*[@id='itemdetails']/div[2]/table/tbody/tr[9]/td").get_attribute('innerHTML')
#     matched_furnished = re.search(r'No|Yes', furnished).group()
#     print(matched_furnished)
#     if matched_furnished == 'Yes':
#         return True
#     else:
#         return False

# def getRoomInfo(paragraph, leaseObj):
#     # spacious rooms
#     # cozy rooms
#     # big rooms, large rooms
#     leaseObj['rooms']['room_desciptions'] = []
#     return leaseObj



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
