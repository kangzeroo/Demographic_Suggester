const Property = require('./routes/property_routes');

module.exports = function(app){
	app.post('/new_kijiji_property', Property.parseAndSave);
	app.post('/filter_query', Property.filterQuery)
}
