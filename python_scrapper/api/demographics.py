def getDemographics(paragraph, leaseObj):
    leaseObj['demographics'] = []
    leaseObj = seniors(paragraph, leaseObj)
    leaseObj = collegeStudents(paragraph, leaseObj)
    leaseObj = youngProfessionals(paragraph, leaseObj)
    leaseObj = impoverishedImmigrants(paragraph, leaseObj)
    leaseObj = investorImmigrants(paragraph, leaseObj)
    leaseObj = youngCouples(paragraph, leaseObj)
    leaseObj = family(paragraph, leaseObj)
    leaseObj = hipYoungsters(paragraph, leaseObj)
    leaseObj = generalDemands(paragraph, leaseObj)
    return leaseObj


def seniors(paragraph, leaseObj):
    try:
        old = re.search(r'(quiet)|(no loud)|(noise)|(senior)|(family friendly)', paragraph, re.I).group()
        print(old)
        leaseObj['demographics'].append(old)
    except:
        print('NOT FOUND ==> # seniors')
        pass

    return leaseObj
    # quiet
    # family
    # safe
    # senior
    # parks nearby
    # gated

def collegeStudents(paragraph, leaseObj):
    try:
        students = re.search(r'(parks)|(near subway)|(downtown(|(core)|(campus)', paragraph, re.I).group()
        print(students)
        leaseObj['demographics'].append(students)
    except:
        print('NOT FOUND ==> # students')
        pass

    return leaseObj
    # bus stops, subway, metro, public transportation
    # close to library
    # campus
    # parks

def youngProfessionals(paragraph, leaseObj):
    try:
        young_workers = re.search(r'(near subway)|(thriving(|(atmosphere)|(near entertainment district)', paragraph, re.I).group()
        print(young_workers)
        leaseObj['demographics'].append(young_workers)
    except:
        print('NOT FOUND ==> # young professionals')
        pass

    return leaseObj
    # public
    # bustling
    # busy
    # thriving
    # booming
    # growing
    # young
    # engaging
    # dynamic
    # lively
    # flourishing
    # developing

def impoverishedImmigrants(paragraph, leaseObj):
    try:
        low_income = re.search(r'(low cost)|(diverse community)', paragraph, re.I).group()
        print(low_income)
        leaseObj['demographics'].append(low_income)
    except:
        print('NOT FOUND ==> # low income')
        pass

    return leaseObj
    # low cost
    # ethnic

def investorImmigrants(paragraph, leaseObj):
    try:
        high_income = re.search(r'(high end)|(gated community)|(uptown)', paragraph, re.I).group()
        print(high_income)
        leaseObj['demographics'].append(high_income)
    except:
        print('NOT FOUND ==> high income')
        pass

    return leaseObj
    # high end
    # uptown

def youngCouples(paragraph, leaseObj):
    try:
        couples = re.search(r'(young professionals)|(build relationships)', paragraph, re.I).group()
        print(couples)
        leaseObj['demographics'].append(couples)
    except:
        print('NOT FOUND ==> # couples')
        pass

    return leaseObj
    # youngProfessionals

def family(paragraph, leaseObj):
    try:
        families = re.search(r'(family friendly)|(parks)|(public school)', paragraph, re.I).group()
        print(families)
        leaseObj['demographics'].append(families)
    except:
        print('NOT FOUND ==> # family')
        pass

    return leaseObj
    # family friendly
    #

def hipYoungsters(paragraph, leaseObj):
    try:
        hipsters = re.search(r'(cultural)|(alive)|(entertainment)|(fresh)|(vibrant)|(thriving)', paragraph, re.I).group()
        print(hipsters)
        leaseObj['demographics'].append(hipsters)
    except:
        print('NOT FOUND ==> # hipsters')
        pass

    return leaseObj
    # musical
    # vibrant

def generalDemands(paragraph, leaseObj):
    try:
        gen_public = re.search(r'(grocery)|(bus)|(mall)', paragraph, re.I).group()
        print(gen_public)
        leaseObj['demographics'].append(gen_public)
    except:
        print('NOT FOUND ==> # General Public')
        pass

    return leaseObj
    # bus stops, subway, metro, public transportation
    # groceries
    # walking distance
    # plaza
