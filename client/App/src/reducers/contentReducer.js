// We import ADD_CONTENT for use inside this reducer
import { ADD_CONTENT, UPDATE_DESC, SET_RESULTS, ADD_PROFILE_TAG } from '../actions/action_types'

// We can define the initial state of this Redux reducer
const INITIAL_STATE = {
	// myContent will be an array of strings
	// myContent will be used by <Home> (ie ../components/home.js) for displaying content
	myContent: [],
	desc: "",
	results: [],
	profile_tags: []
}

// The Redux reducer is simply a function that takes 2 attributes: (state, action)
export default function(state = INITIAL_STATE, action){
	// This switch statement checks the incoming action for the `type` attribute
	switch(action.type){
		// If `action.type == ADD_CONTENT`, then..
		case ADD_CONTENT:
			return {
				// return all the attributes of state (using ES6 object deconstructors `...state`)
				...state,
				// and overwrite the `myContent` attribute with the old `myContent` array concatenated with the new action.payload value
				myContent: state.myContent.concat([action.payload])
			}
		case UPDATE_DESC:
			return {
				...state,
				desc: action.payload
			}
		case SET_RESULTS:
			return {
				...state,
				results: action.payload,
				profile_tags: []
			}
		case ADD_PROFILE_TAG:
			return {
				...state,
				profile_tags: action.payload
			}
	}
	// for all uncaught `action.type`, just return the state
	return state
}

// This Redux reducer is exported for use in `./index.js`, to be combined with other reducers to form a giant combined reducer
// See `./index.js` for more details
