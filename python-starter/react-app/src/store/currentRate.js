const GET_CURRENT_RATE = "currentRate/GET_CURRENT_RATE";

const getRate = (fxRate) => {
  return {
    type: GET_CURRENT_RATE,
    fxRate,
  };
};



export const getCurrentRateThunk = (currencyPair) => async (dispatch) => {
  const pairArray = currencyPair.split("/");
  const base = pairArray[0];
  const quote = pairArray[1];
  const data = await fetch(`/api/currency/${base}/${quote}`);
  const response = await data.json();
  dispatch(getRate(response));
  return;
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
