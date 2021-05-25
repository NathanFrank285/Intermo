const GET_TRADES = 'trades/GET_TRADES';
// const NEW_TRADE = "trades/NEW_TRADE";

const getTrades = (trades) => {
  return {
    type: GET_TRADES,
    trades
  }
}

// const newTrade = (trade) => {
//   return {
//     type: NEW_TRADE,
//     trade
//   }
// }

export const getTradesThunk = () => async (dispatch) => {
  const data = await fetch('/api/trade')
  const response = await data.json()
  dispatch(getTrades(response))
}

export const newTradeThunk = (newTrade) => async (dispatch) => {
  let data = await fetch("/api/trade/newTrade", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(newTrade),
  });
  const response = await data.json()

  return response
}



let initialState = {}
const trades = (state=initialState, action) => {
  switch (action.type) {
    case GET_TRADES:
      return { ...state, ...action.trades };
    default:
      return state;
  }
}
export default trades
