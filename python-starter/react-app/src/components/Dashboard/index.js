import React, {useState} from "react";
import { useDispatch, useSelector } from "react-redux";
import "./Dashboard.css";

// todo create the search bar with buy and sell buttons below, the trade history table on the bottom left and the portfolio allocation graph on the right
// todo
function Dashboard() {
  const user = useSelector(state => state?.session?.user)
  const [searchValue, setSearchValue] = useState('')
  const [quantity, setQuantity] = useState('')
  const [direction, setDirection] = useState('')
  console.log(quantity)
  return (
      <div>
        {user && user ? (<h1>Hello {user.username}, what would you like to convert today?</h1>) : (<h1>Hello, welcome to the Dashboard</h1>)}
      <div className="dashboard-container">
      <div className="searchBar">
        <label>
          What Currency would you like to convert?
        </label>
        <input
        type="search"
        value={searchValue}
        onChange={(e)=>setSearchValue(e.target.value)}
        ></input>
        <br></br>
        <label>How much do you want to convert?</label>
        <input
        type="number"
        value={quantity}
        onChange={(e)=>setQuantity(e.target.value)}
        ></input>
        <div className="buySellButtonContainer">
          <div className="button buyButton">Buy</div>
          <div className="button sellButton">Sell</div>
        </div>
      </div>
      <div className="historicalTrades">

      </div>
      <div className="portfolioAllocation">

      </div>


      </div>
      </div>
  );
}

export default Dashboard;
