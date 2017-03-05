// See <App> (ie ./app.js) to read documentation on how a React component works
import React, {Component} from 'react';
import {connect} from 'react-redux';
import Radium from 'radium'
import {setResultsFilteredFromKijiji} from '../../actions/contentActions'
import {getFilteredResults} from '../../api/myAPI'


class PopupQuery extends Component {

		constructor(){
			super()
			this.state = {
				desc: ""
			}
		}

    setDescription(event){
      this.setState({
        desc: event.target.value
      })
    }

    submitQuery(){
      getFilteredResults(this.state.desc)
        .then((data)=>{
          this.props.setResultsFilteredFromKijiji(data)
        })
    }

		render() {
			return (
				<div style={comStyles().mainview}>
          <textarea value={this.state.desc} onChange={this.setDescription.bind(this)} style={comStyles().textareaBox}  placeholder="Tell me about yourself" required></textarea>
          <button className='btn btn-primary' onClick={this.submitQuery.bind(this)} style={comStyles().submitButton}>SEARCH</button>
				</div>
			)
		}
}

PopupQuery.propTypes = {
	// something: React.PropTypes.object,
	// someAction: React.PropTypes.func.isRequired
}

function mapStateToProps(state){
	return {
		// something: state.something
	}
}

const RadiumHOC = Radium(PopupQuery)

export default connect(
	null,
	{setResultsFilteredFromKijiji}
)(RadiumHOC)

// ================================

const comStyles = () => {
	return {
		mainview: {
			width: '60vw',
      height: '15vh',
      margin: '0px auto',
      display: 'flex',
      flexDirection: 'row',
			padding: "20px"
		},
    textareaBox: {
      flexGrow: 5,
      padding: '15px',
      fontSize: '1.2rem',
      fontWeight: 'bold'
    },
    submitButton: {
      flexGrow: 1
    }
	}
}
