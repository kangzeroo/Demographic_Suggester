// See <App> (ie ./app.js) to read documentation on how a React component works
import React, {Component} from 'react';
import {connect} from 'react-redux';
import Radium from 'radium'
import { filterRegex } from '../../api/regexr'
import { updateProfileTagsFound } from '../../actions/contentActions'

class LiveProfile extends Component {

    constructor(){
      super()
      this.state = {
        show: true
      }
    }

    shouldComponentUpdate(nextProps, nextState){
      if(nextProps.profile_tags == [] || nextProps.profile_tags == this.props.profile_tags){
        return true
      }else{
        return false
      }
    }

		componentDidUpdate(){
			filterRegex(this.props.desc)
				.then((tags)=>{
          this.props.updateProfileTagsFound(tags)
				})
		}

    showTags(){
      const tags = []
      this.props.profile_tags.forEach((t)=>{
        const tag = (<div>{t.tag_word}</div>)
        tags.push(tag)
      })
      return tags
    }

    exitButton(){
      return (
        <button className='btn btn-info' onClick={()=>this.setState({show: false})} style={comStyles().exitButton}>Close</button>
      )
    }

		render() {
			return (
        <div>
          {
            this.state.show && this.props.profile_tags.length > 0
            ?
    				<div style={comStyles().mainview}>
    					{this.showTags()}
              {this.exitButton()}
    				</div>
            :
            null
          }
        </div>
			)
		}
}

LiveProfile.propTypes = {
  desc: React.PropTypes.string.isRequired,
  profile_tags: React.PropTypes.array
}

function mapStateToProps(state){
	return {
		desc: state.content.desc,
    profile_tags: state.content.profile_tags
	}
}

const RadiumHOC = Radium(LiveProfile)

export default connect(
	mapStateToProps,
	{updateProfileTagsFound}
)(RadiumHOC)

// ================================

const comStyles = () => {
	return {
		mainview: {
			textAlign: "center",
			padding: "10px",
      width: '60vw',
      margin: '0px auto',
      fontSize: '1.3rem',
      fontWeight: 'bold',
      backgroundColor: 'rgba(98, 145, 216, 0.7)',
      color: 'white',
      lineHeight: '25px',
      borderRadius: '50px'
		},
    exitButton: {
      margin: '15px'
    }
	}
}
