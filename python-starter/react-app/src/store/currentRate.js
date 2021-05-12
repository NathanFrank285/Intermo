const GET_CURRENT_RATE = "currentRate/GET_CURRENT_RATE";

const getRate = (fxRate) => {
  return {
    type: GET_CURRENT_RATE,
    fxRate,
  };
};



export const getCurrentRateThunk= (currencyPair) => async (dispatch) => {

}

let initialState = {}
const currentRate = (state=initialState, action) => {
  switch (action.type) {
    case GET_CURRENT_RATE:
      return {...action.fxRate}
    default:
      return state
  }
}
export default currentRate
