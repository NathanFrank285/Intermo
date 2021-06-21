import React,{useEffect} from "react";
import { useDispatch } from "react-redux";
import './ViewTheMarket.css'

function ViewTheMarket() {
  const dispatch = useDispatch();

  useEffect(() => {
    // dispatch(getAllOffers())
  },[])


  return (
    <div>
      <h1 className='header'>I am the View the Market page</h1>
    </div>
  )
}


export default ViewTheMarket;
