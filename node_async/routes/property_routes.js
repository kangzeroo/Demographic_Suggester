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
}

// POST /filter_query
exports.filterQuery = function(req, res, next){
	Property.find({}, function(err, props){
		if(err){console.log(err)};
		//console.log(leases);
		// return the matching Leases
		if(props.length > 0){
			res.json(props);
		}else{
			res.json([]);
		}
	})
}
