const GET_USER_BALANCE = "userBalance/GET_USER_BALANCE";

const getUserBalance = (userBalance) => {
  return {
    type: GET_USER_BALANCE,
    userBalance,
  };
};

export const getUserBalanceThunk = (searchData) => async (dispatch) => {
  const data = await fetch(`/api/userBalance`);
  const response = await data.json();
  dispatch(getUserBalance(response));
  return;
};

let initialState = {};
const userBalance = (state = initialState, action) => {
  switch (action.type) {
    case GET_USER_BALANCE:
      return { ...action.userBalance };
    default:
      return state;
  }
};
export default userBalance;
