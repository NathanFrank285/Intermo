const GET_TRADES = 'trades/GET_TRADES';

const getTrades = (trades) => {
  return {
    type: GET_TRADES,
    trades
  }
}

export const getTradesThunk = () => async (dispatch) => {
  const data = await fetch('/api/trade')
  const response = await data.json()
  dispatch(getTrades(response))
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
