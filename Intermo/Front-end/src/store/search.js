const SAVE_SEARCH = 'search/SAVE_SEARCH'


export const saveSearch = (searchResults) => {
  return {
    type: SAVE_SEARCH,
    searchResults,
  };
};


let initialState = {};
const search = (state = initialState, action) => {
  switch (action.type) {
    case SAVE_SEARCH:
      return { ...action.searchResults };
    default:
      return state;
  }
};
export default search;
