const GET_MARKET_RATES = "currentRate/GET_MARKET_RATES";

const getMarketRates = () => {
  return {
    type: GET_MARKET_RATES,
    marketRates,
  };
};

export const getMarketRatesThunk = (currencyPair) => async (dispatch) => {
  // const pairArray = currencyPair.split("/");
  // const base = pairArray[0];
  // const quote = pairArray[1];
  // const data = await fetch(`/api/currency/${base}/${quote}`);
  // const response = await data.json();
  // dispatch(getRate(response));
  // return;
};

let initialState = {};
const currentRate = (state = initialState, action) => {
  switch (action.type) {
    case GET_MARKET_RATES:
      return { ...action.fxRate };
    default:
      return state;
  }
};
export default currentRate;
