// Import dependencies on Mongoose
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// Create the Property schema
var PropertySchema = new mongoose.Schema({
  "kijiji_link": String,
  "meta": {
      "active": Boolean,       // if should be shown on map
      "claimed": Boolean,     // if property has been claimed by a landlord
      "deleted": Boolean,      // if property was deleted
      "added_at": Date
  },
  "coords": [Number],
  "core": {
      "city": String,
      "property_type": String,
      "thumbnail": String,
      "note": String,
      "posted_at": Number,
      "whole_price": Number,
      "address": String,
      "owner": String,
      "place_id": String,
      "kijiji_id": String
  },
  "rooms": [{
      "room_type": String,
      "price": Number,
      "rooms_per": Number,
      "lease_terms": Number,
      "bathrooms": Number,
      "room_desciptions": [String]
  }],
  "utils_list": {
      "water": Boolean,
      "heat": Boolean,
      "electric": Boolean,
      "internet": Boolean,
      "furnished": Boolean,
      "parking": Boolean,
      "free_parking": Boolean,
      "ac": Boolean,
      "gym": Boolean,
      "laundry": Boolean
  },
  "demographics": [String],
  "nearby": [String],
  "contacts": [{
    "name": String,
    "phone": String,
    "email": String
  }],
  "images": [{
    imageKey: String,
    thumbnailUrl: String,
    originalUrl: String
  }]
});

PropertySchema.pre('save', function(next){
	var currentDate = new Date();

	this.meta.added_at = currentDate;
	next();
});

PropertySchema.index({coords: '2dsphere'});

var Property = mongoose.model('Property', PropertySchema);

module.exports = Property;
