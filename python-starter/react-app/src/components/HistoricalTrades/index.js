import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getTradesThunk } from "../../store/trades";
import './HistoricalTrades.css'

function HistoricalTrades() {
  const dispatch = useDispatch();
  const trades = useSelector(state=>state?.trades)

  useEffect(() => {
    dispatch(getTradesThunk());
    // eslint-disable-next-line
  },[])

  // bidOrOffer: "bid";
  // created_on: "Wed, 05 May 2021 00:00:00 GMT";
  // id: 2;
  // makerCurrencyId: 3;
  // makerId: 2;
  // price: 1.6864;
  // quantity: 120;
  // takerCurrencyId: 1;
  // takerId: 1;
  //todo: paginate the trade data
  const tradeKeys = Object.keys(trades)
  const rows = tradeKeys?.map((tradeKey, id)=>{
    let date = new Date(trades[`${tradeKey}`]["created_on"]).toLocaleDateString()
    let direction = trades[`${tradeKey}`]["bidOrOffer"] === 'bid' ? 'Buy' : 'Sell';
    return (
      <tr key={id}>
        <td>{date}</td>
        <td>{direction}</td>
        <td>{trades[`${tradeKey}`]["name"]}</td>
        <td>{trades[`${tradeKey}`]["quantity"]}</td>
        <td>{trades[`${tradeKey}`]["price"]}</td>
      </tr>
    );
  })

  return (
    <div className="tradeHistory-container">
      <h2 className="tradeHistory">Trade history</h2>
      <table>
        <tbody>
          <tr>
            <th>Date</th>
            <th>Side</th>
            <th>Currencies</th>
            <th>Quantity</th>
            <th>Price</th>
          </tr>
          {trades && Object.keys(trades).length > 0
            ? rows
            : "No trade data available"}
        </tbody>
      </table>
    </div>
  );

}

export default HistoricalTrades;
