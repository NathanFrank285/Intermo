const GET_POSTS = 'posts/GET_POSTS'

const getPosts = (searchResults) => {
  return {
    type: GET_POSTS,
    searchResults
  }
}


export const getPostsThunk = (searchData) => async (dispatch) => {
  const datat = await fetch('/api/post')
}
