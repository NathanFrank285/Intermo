import React, {useState, useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import HistoricalTrades from '../HistoricalTrades'
import PortfolioGraph from '../PortfolioGraph'
import "./Dashboard.css";

// todo create the search bar with buy and sell buttons below, the trade history table on the bottom left and the portfolio allocation graph on the right
// todo
function Dashboard() {
  const dispatch = useDispatch()
  const user = useSelector(state => state?.session?.user)
  const [baseSearchValue, setBaseSearchValue] = useState('')
  const [quoteSearchValue, setQuoteSearchValue] = useState('')
  const [quantity, setQuantity] = useState('')

  const findPosts = (direction) => {
    console.log(baseSearchValue, quoteSearchValue, quantity, direction)
    const searchData = {
      baseSearchValue,
      quoteSearchValue,
      quantity,
      direction
    }
    // dispatch(getPostsThunk(searchData))
  }
  function setSell() {
    setDirection('sell')
    findPosts()
  }

  return (
    <div>
      <h2>Welcome, what would you like to convert today?</h2>
      <div className="dashboard-container">
        <div className="searchBar">
          <label>What Currency would you like to convert?</label>
          <input
            type="search"
            value={baseSearchValue}
            onChange={(e) => setBaseSearchValue(e.target.value)}
          ></input>
          <br></br>
          <label>What Currency would you like in return?</label>
          <input
            type="search"
            value={quoteSearchValue}
            onChange={(e) => setQuoteSearchValue(e.target.value)}
          ></input>
          <br></br>
          <label>How much do you want to convert?</label>
          <input
            type="number"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
          ></input>
          <div className="buySellButtonContainer">
            <div
              className="button buyButton"
              onClick={()=>findPosts('buy')}
              >
              Buy
            </div>
            <div
              className="button sellButton"
              onClick={()=>findPosts('sell')}
            >
              Sell
            </div>
          </div>
        </div>
        <div className="historicalTrades">
          <HistoricalTrades />
        </div>
        <div className="portfolioAllocation">
          <PortfolioGraph />
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
