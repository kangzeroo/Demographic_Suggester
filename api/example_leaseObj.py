
def getDefault():
    return default_leaseObj

default_leaseObj = {
    "kijiji_link": "http://www.kijiji.ca/v-house-rental/kitchener-waterloo/waterloo-townhome-for-rent-laurelwood/1241107253?uli=true",
    "meta": {
        "active": True,       # if should be shown on map
        "claimed": False,     # if property has been claimed by a landlord
        "deleted": False      # if property was deleted
    },
    "core": {
        "city": "",
        "property_type": "",
        "thumbnail": "",
        "note": "",
        "posted_at": 0,
        "whole_price": 0,
        "address": "",
        "owner": "",
        "coords": [],
        "place_id": ""
    },
    "rooms": [{
        "room_type": "Avg Room",
        "price": 0,
        "rooms_per": 0,
        "lease_terms": 0,
        "bathrooms": 0,
        "room_desciptions": []
    }],
    "utils_list": {
        "water": False,
        "heat": False,
        "electric": False,
        "internet": False,
        "furnished": False,
        "parking": False,
        "free_parking": False,
        "ac": False,
        "gym": False,
        "laundry": False
    },
    "demographics": [],
    "nearby": [],
    "images": []
}

example_leaseObj = {
    "kijiji_link": "http://www.kijiji.ca/v-house-rental/kitchener-waterloo/waterloo-townhome-for-rent-laurelwood/1241107253?uli=true",
    "meta": {
        "active": True,       # if should be shown on map
        "claimed": False,     # if property has been claimed by a landlord
        "deleted": False      # if property was deleted
    },
    "core": {
        "city": "Toronto",
        "property_type": "House",
        "thumbnail": "https://s3.amazonaws.com/rentburrow-images/ideas%2540bytenectar.io/default_home_icon.png",
        "note": "Bright, clean and extremely well maintained executive town home in the quiet, family friendly neighborhood of sought after Laurelwood. Available immediately! This three bedroom, three bath home features a stunning grand entrance with 16 foot cathedral ceiling. The main floor is open concept, painted in neutral colours, and offers a large eat in kitchen, family room, two piece bath, inside entry from the garage, and walk out to deep back yard. The second level offers a large master bedroom with four piece ensuite and walk in closet. Two more generous sized bedrooms and an additional four piece bathroom complete this level. Prime location close to great schools, shopping, RIM, the university, public transit, and conservation lands with an abundance of walking / biking trails. Beautifully landscaped and maintained, youll be proud to call this one home. $1500 per month plus utilities. Credit check, references, income verification required.",
        "posted_at": 3690568896,
        "whole_price": 1500,
        "address": "571 Wild Iris Ave, Waterloo, ON N2V 2X5, Canada",
        "owner": "Private Landlord",
        "coords": [-34.345364, 80.435645],
        "place_id": "FJFD9230Hk"
    },
    "rooms": [{
        "room_type": "Standard",
        "price": 600,
        "rooms_per": 3,
        "lease_terms": 12,
        "bathrooms": 2,
        "room_desciptions": ["generous"]
    }],
    "utils_list": {
        "water": True,
        "heat": True,
        "electric": True,
        "internet": True,
        "furnished": True,
        "parking": True,
        "free_parking": False,
        "ac": True,
        "gym": False,
        "laundry": True
    },
    "demographics": ["young_residents", "high_income", "tag1", "tag2", "tagN"],
    "nearby": ["parks", "hospital", "metro"],
    "images": [
        "https://s3.amazonaws.com/rentburrow-images/ideas%2540bytenectar.io/default_home_icon.png"
    ]
}
