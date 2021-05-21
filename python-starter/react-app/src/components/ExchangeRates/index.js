import React from "react";
import { /* useDispatch */ useSelector } from "react-redux";
import "./ExchangeRates.css";

function ExchangeRates() {
  // const dispatch = useDispatch()
  const currentRate = useSelector(state=>state?.currentRate?.rate)


  return (
    <>
      {currentRate && <p>The current rate is {currentRate}</p>}
    </>
  );
}

export default ExchangeRates;
