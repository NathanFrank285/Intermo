import React, {useState, useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useHistory } from "react-router-dom";
import {getPostsThunk} from '../../store/posts'
import { getCurrenciesThunk } from '../../store/pairs';
import HistoricalTrades from '../HistoricalTrades'
import PortfolioGraph from '../PortfolioGraph'
import "./Dashboard.css";
// import CurrentRateSlider from "../CurrentRateSlider";

// todo create the search bar with buy and sell buttons below, the trade history table on the bottom left and the portfolio allocation graph on the right

function Dashboard() {
  const dispatch = useDispatch()
  const history = useHistory()
  const user = useSelector(state => state?.session?.user)
  const pairs = useSelector(state => state?.pairs[0])
  const [pair, setPairSearchValue] = useState('EUR/USD')
  const [quantity, setQuantity] = useState('')
  const [direction, setDirection] = useState('bid')

  useEffect(() => {
    dispatch(getCurrenciesThunk());
    // eslint-disable-next-line
  },[])

  const findPosts = () => {
    const searchData = {
      pair,
      quantity,
      direction
    }
    dispatch(getPostsThunk(searchData))
    history.push("/posts");
  }

  return (
    <div>
      {/* <CurrentRateSlider/> */}
      <div className="title-container">
        <h2 className="dashboardTitle">
          Welcome to Intermo! The only community driven place to exchange
          foreign currencies.{" "}
        </h2>
      </div>
      <div className="dashboard-container">
        <form className="formContainer" onSubmit={findPosts}>
          <div className="searchBar">
            <span>To get started, what pair would you like to convert?</span>
            <br></br>
            <select
              required
              onChange={(e) => setPairSearchValue(e.target.value)}
              className="form-element"
            >
              {pairs &&
                pairs.map((pair) => (
                  <option key={pair["id"]} value={pair["name"]}>
                    {pair["name"]}
                  </option>
                ))}
            </select>
            <br></br>
            <label>How much do you want to convert?</label>
            <br></br>
            <input
              required
              type="number"
              value={quantity}
              onChange={(e) => setQuantity(e.target.value)}
              className="form-element"
            ></input>
            <br></br>
            <label>Do you want to buy or sell?</label>
            <br></br>
            <select
              onChange={(e) => setDirection(e.target.value)}
              className="form-element"
            >
              <option value="bid">Buy</option>
              <option value="offer">Sell</option>
            </select>
            <br></br>
            <button type="submit" className="form-button">
              Search
            </button>
          </div>
        </form>

        {user ? (
          <>
            <div className="historicalTrades">
              <HistoricalTrades />
            </div>
            <div className="portfolioAllocation">
              <PortfolioGraph />
            </div>{" "}
          </>
        ) : (
          <div className="loginLink">
            <NavLink className="loginLink-link" to="/login">
              Please login to view past trades and current balances
            </NavLink>
          </div>
        )}
      </div>
    </div>
  );
}

export default Dashboard;
