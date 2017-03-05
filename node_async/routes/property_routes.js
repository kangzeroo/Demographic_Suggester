const Property = require('../models/property_model');
const parseGPS = require('../api/googleMaps').parseGPS
const savePropertyToDb = require('../api/saveProperty').savePropertyToDb

// POST /new_kijiji_property
exports.parseAndSave = function(req, res, next){

	console.log("....................New Kijiji Property.......................")

	parseGPS(req.body)
		.then((property)=>{
			return savePropertyToDb(property)
		})
		.then((data)=>{
			console.log(data)
			res.json({message: "success"})
		})
		.catch((err)=>{
			console.log(err)
			res.send.error(500)
		})
};
