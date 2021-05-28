// get the historical trade data and the account balance

const GET_CURRENCIES = 'currencies/GET_CURRENCIES';

const getCurrencies = (currencies) => {
  return {
    type: GET_CURRENCIES,
    currencies
  }
}


export const getCurrenciesThunk = () => async (dispatch) => {
  const data = await fetch(`/api/currency`);
  const response = await data.json();
  dispatch(getCurrencies(Object.values(response)));
  return;
}

let initialState = {};
const pairs = (state = initialState, action) => {
  switch (action.type) {
    case GET_CURRENCIES:
      return { ...state, ...action.currencies };
    default:
      return state;
  }
};
export default pairs;
