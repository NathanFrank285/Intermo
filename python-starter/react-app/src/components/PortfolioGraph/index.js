import React, { useState, useEffect } from "react";
import { getUserBalanceThunk } from '../../store/userBalance';
import { useDispatch, useSelector } from "react-redux";
import * as d3 from "d3";

function PortfolioGraph() {
  const dispatch = useDispatch();
  const userBalance = useSelector(state => state?.userBalance?.balances)

  console.log(userBalance, "---- I am the user balance")
  useEffect(() => {
    dispatch(getUserBalanceThunk());
  },[])

  return (
    <div>
      <h2>I am the portfolio graph component</h2>
      <div className="pieChart"></div>
    </div>
  );
}

export default PortfolioGraph;
