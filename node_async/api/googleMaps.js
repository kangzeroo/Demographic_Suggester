const GoogleMapsAPI = require('googlemaps')

exports.parseGPS = function(leaseObj){
	const p = new Promise((res, rej)=>{
		const publicConfig = {
		  key: 'AIzaSyB2fN0DvaoUeEqYIDRMVSvPjXI0lgtBiSY',
		  stagger_time:       1000, // for elevationPath
		  encode_polylines:   false,
		  secure:             true // use https
		  //proxy:              'http://127.0.0.1:9999' // optional, set a proxy for HTTP requests
		}
		const gmAPI = new GoogleMapsAPI(publicConfig);

		// geocode API
		const geocodeParams = {
		  "address": leaseObj.core.address,
		  "components": "components=country:CA"
		}

		gmAPI.geocode(geocodeParams, function(err, result){
		  if(err){console.log(err)};
		   //console.log(result);
		  if(result){
        console.log(result)
		  	if(result.results[0]){
			  	// take the coords of the first result
			  	leaseObj.coords = [parseFloat(result.results[0].geometry.location.lng.toFixed(7)), parseFloat(result.results[0].geometry.location.lat.toFixed(7))];
					leaseObj.core.place_id = result.results[0].place_id
			  	res(leaseObj);
			}else{
				console.log(leaseObj.core.address)
				console.log(result)
			  	rej("No geocoding data!");
			}
		  }
		})
	})
	return p
}
