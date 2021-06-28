import React,{useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import { getCurrenciesThunk } from "../../store/pairs";
import { getAllOffersThunk } from "../../store/posts";

import './ViewTheMarket.css'

function ViewTheMarket() {
  const dispatch = useDispatch();
  const allPairs = useSelector(state => state?.posts?.posts)
  

  useEffect(() => {
    dispatch(getAllOffersThunk())
    dispatch(getCurrenciesThunk());
  },[])


  return (
    <div>
      <h1 className='header'>I am the View the Market page</h1>
    </div>
  )
}


export default ViewTheMarket;
