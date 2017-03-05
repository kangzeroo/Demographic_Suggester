import React, {Component} from 'react'
import {connect} from 'react-redux'
import Radium from 'radium'
import PopupQuery from './popup_query'
import LiveProfile from './liveload_profile'

class MapView extends Component {

	constructor(){
		super()
		this.state = {
			mapview: null
		}
		this.pins = []
		this.recolorRed.bind(this)
		this.highlightPin.bind(this)
		this.refreshPins.bind(this)
	}

	componentDidMount(){
		if(this.props.rootView){
			google.maps.event.addDomListener(window, "load", this.mountGoogleMap.bind(this))
		}else{
			this.mountGoogleMap()
		}
	}

	componentDidUpdate(){
		this.recolorRed()
	  this.refreshPins(this.props.results)
	}

	mountGoogleMap(){
		let coords = {lat: 43.663614, lng: -79.386284}
		if(this.props.preDefinedCoords){
			coords = this.props.preDefinedCoords
		}
		let mapOptions = {
	        center: coords,
	        zoom: 14
	    }
	    if(this.props.mobileViewer){
	    	mapOptions = {
	    		...mapOptions,
	    		disableDefaultUI: true
	    	}
	    }
		const mapview = new google.maps.Map(document.getElementById('mapview'), mapOptions)
	    this.setState({
	    	mapview: mapview
	    })
	}

	// map the pins on every update
	refreshPins(newPins){
  	const self = this
  	this.clearPins()
  	newPins.forEach((n,i)=>{
  		let marker
      marker = new google.maps.Marker({
          position: new google.maps.LatLng(n.coords[1], n.coords[0]),
          //map: self.state.mapview,
          icon: "../../../res/images/red-dot.png"
      });
      marker.cardId = n._id
    // action on click of pin
    google.maps.event.addListener(marker, 'click', function(e){
			const win = window.open(n.kijiji_link, '_blank');
  		win.focus();
    })
    self.pins.push(marker)
  })
  self.pins.forEach((pin, index)=>{
  	pin.setMap(self.state.mapview)
  })
}

	clearPins(){
		if(this.pins){
			this.pins.forEach((pin)=>{
				pin.setMap(null)
			})
			this.pins.length = 0
		}
	}

	highlightPin(marker){
		this.recolorRed()
		// and color the desired marker blue
	    for(let m = 0; m<this.pins.length; m++){
	        if(this.pins[m].position.lat().toFixed(7) == marker.position.lat().toFixed(7) && this.pins[m].position.lng().toFixed(7) == marker.position.lng().toFixed(7)){
	          this.pins[m].setIcon("../../../res/images/blue-dot.png")
	        }
	    }
	    // pan the map view to blue marker
	    this.state.mapview.panTo(marker.position)
	}

  recolorRed(){
		if(this.pins){
			for(let m = 0; m<this.pins.length; m++){
		     this.pins[m].setIcon("../../../res/images/red-dot.png")
		  }
		}
	}

	render() {
		return (
      <div style={comStyles().container}>
			   <div id="queryBox" style={comStyles().queryBox}>
            <PopupQuery />
						<LiveProfile />
         </div>
			   <div id="mapview" style={comStyles().mapview}></div>
      </div>
		)
	}
}

MapView.propTypes = {
	results: React.PropTypes.array
}

const RadiumHOC = Radium(MapView)

function mapStateToProps(state){
	return {
		results: state.content.results
	}
}

export default connect(mapStateToProps)(RadiumHOC)


// =====================================
const comStyles = () => {
	return {
    container: {
      width: '100vw',
      height: '100vh'
    },
		mapview: {
			width: "100%",
			height: "100%"
		},
    queryBox: {
      zIndex: 10,
      position: 'absolute',
      right: '10px',
			display: 'flex',
			flexDirection: 'column'
    }
	}
}
