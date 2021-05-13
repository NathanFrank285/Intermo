import React from "react";
import { useDispatch, useSelector } from "react-redux";
import "./ExchangeRates.css";

function ExchangeRates() {
  const dispatch = useDispatch()
  const currentRate = useSelector(state=>state?.currentRate)
  return (
    <>
      <h1>No exchange rate data</h1>
    </>
  );
}

export default ExchangeRates;
