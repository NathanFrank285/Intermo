import {saveSearch} from './search'

const GET_POSTS = 'posts/GET_POSTS'

const getPosts = (searchResults) => {
  return {
    type: GET_POSTS,
    searchResults
  }
}

export const getPostsThunk = (searchData) => async (dispatch) => {
  const {base, quantity, direction} = searchData
  const data = await fetch(`/api/post/${base}/${quantity}/${direction}`)
  const response = await data.json()
  dispatch(getPosts(response))
  dispatch(saveSearch(searchData))
  return
}

export const newPostThunk = (newPost) => async (dispatch) => {
  const data = await fetch("/api/post", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(newPost),
  });
  const response = await data.json()
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
