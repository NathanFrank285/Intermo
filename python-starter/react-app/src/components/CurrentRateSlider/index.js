import React from "react";
import { useDispatch } from "react-redux";
import { getMarketRatesThunk } from "../../store/rateSlider";


function CurrentRateSlider() {
  const dispatch = useDispatch();

  dispatch(getMarketRatesThunk());

  return(
    <h2>I am the currency rates slider</h2>
  )
}
export default CurrentRateSlider
