import React, {useState, useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import {getPostsThunk} from '../../store/posts'
import { getCurrenciesThunk } from '../../store/pairs';
import HistoricalTrades from '../HistoricalTrades'
import PortfolioGraph from '../PortfolioGraph'
import "./Dashboard.css";

// todo create the search bar with buy and sell buttons below, the trade history table on the bottom left and the portfolio allocation graph on the right
// todo
function Dashboard() {
  const dispatch = useDispatch()
  const history = useHistory()
  const user = useSelector(state => state?.session?.user)
  const pairs = useSelector(state => state?.pairs[0])
  const [base, setBaseSearchValue] = useState(1)
  const [quote, setQuoteSearchValue] = useState('')
  const [quantity, setQuantity] = useState('')
  const [direction, setDirection] = useState('bid')

  useEffect(() => {
    dispatch(getCurrenciesThunk())
  },[])

  const findPosts = () => {
    console.log(base, quantity, direction)
    const searchData = {
      base,
      quantity,
      direction
    }
    dispatch(getPostsThunk(searchData))
    history.push("/posts");
  }
  if (pairs) {
    console.log("---------", pairs)
  }
  return (
    <div>
      <h2>Welcome, what would you like to convert today?</h2>
      <div className="dashboard-container">
        <form onSubmit={findPosts}>
          <div className="searchBar">
            <label>What pair would you like to convert?</label>
            <select
              required
              onChange={(e) => setBaseSearchValue(e.target.value)}
            >
              {pairs &&
                pairs.map((pair) => (
                  <option key={pair["id"]} value={pair["id"]}>
                    {pair['name']}
                  </option>
                ))}
            </select>
            <br></br>
            <label>How much do you want to convert?</label>
            <input
              required
              type="number"
              value={quantity}
              onChange={(e) => setQuantity(e.target.value)}
            ></input>
            <div className="buySellButtonContainer">
              <select onChange={(e) => setDirection(e.target.value)}>
                <option value="bid">Buy</option>
                <option value="offer">Sell</option>
              </select>
            </div>
            <button type="submit">Search</button>
          </div>
        </form>
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
