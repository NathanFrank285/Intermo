import {saveSearch} from './search'
import {getCurrentRateThunk} from './currentRate'

const GET_POSTS = 'posts/GET_POSTS'

const getPosts = (searchResults) => {
  return {
    type: GET_POSTS,
    searchResults
  }
}

export const getPostsThunk = (searchData) => async (dispatch) => {
  const {pair, quantity, direction} = searchData
  const pairArray = pair.split('/')
  const base = pairArray[0]
  const quote = pairArray[1]
  delete searchData.pair
  searchData.base = base
  searchData.quote = quote

  //todo split pair and send that to the back end
  const data = await fetch(`/api/post/${base}/${quote}/${quantity}/${direction}`)
  const response = await data.json()
  dispatch(getPosts(response))
  dispatch(saveSearch(searchData))
  dispatch(getCurrentRateThunk(pair));
  return
}

export const newPostThunk = (newPost) => async (dispatch) => {
  const response = await fetch("/api/post/new", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(newPost),
  });
  const data = await response.json()
  console.log(data)
}

let initialState = {}
const posts = (state=initialState, action) => {
  switch (action.type) {
    case GET_POSTS:
      return {...action.searchResults}
    default:
      return state
  }
}
export default posts
