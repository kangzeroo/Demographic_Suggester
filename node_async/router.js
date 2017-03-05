const Property = require('./routes/property_routes');

module.exports = function(app){
	// Auth related routes
	app.post('/new_kijiji_property', Property.parseAndSave);
}
