import React, {useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import "./ExchangeRates.css";

function ExchangeRates() {
  const dispatch = useDispatch()
  const currentRate = useSelector(state=>state?.currentRate?.rate)

  useEffect(() => {

  },[])

  return (
    <>
      {currentRate && (
      <p>The current exchange rate is {currentRate}. Make sure that you choose a rate that is close to the current price.</p>

      )}
    </>
  );
}

export default ExchangeRates;
