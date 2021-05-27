const GET_MARKET_RATES = "currentRate/GET_MARKET_RATES";

// const getMarketRates = (marketRates) => {
//   return {
//     type: GET_MARKET_RATES,
//     marketRates,
//   };
// };

export const getMarketRatesThunk = () => async (dispatch) => {

  const data = await fetch(`/api/currency/MarketRates`);
  // const response = await data.json();
  // console.log(response);
  // dispatch(getMarketRates(response));
  return;
};

let initialState = {};
const marketRates = (state = initialState, action) => {
  switch (action.type) {
    case GET_MARKET_RATES:
      return { ...action.fxRate };
    default:
      return state;
  }
};
export default marketRates;
