import React from "react";
import { exchangeRates } from "exchange-rates-api";
import "./ExchangeRates.css";

function ExchangeRates() {

  // let exchangeRate = 0
  // const query = async () => {
  //   const data = await exchangeRates().latest().fetch();
  //   // exchangeRate = data
  //   console.log(data.GBP)
  //   return data.GBP
  // }
  // exchangeRate = query()

  return (
    <>
      <h1>No exchange rate data</h1>
    </>
  );
}

export default ExchangeRates;
