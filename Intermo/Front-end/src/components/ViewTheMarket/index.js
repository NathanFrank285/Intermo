import React,{useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import { getCurrenciesThunk } from "../../store/pairs";
import { getAllOffersThunk } from "../../store/posts";

import './ViewTheMarket.css'

function ViewTheMarket() {
  const dispatch = useDispatch();
  let posts = useSelector(state => state?.posts?.posts)
  let pairs = useSelector(state => state?.pairs)


  useEffect(() => {
    dispatch(getAllOffersThunk())
    dispatch(getCurrenciesThunk());
  },[])

  let numberOfPosts;
  let postValues;
  let pairsObject = {}


  if (posts && pairs) {
    numberOfPosts = Object.entries(posts).length;
    let postArray = Object.entries(posts);


    for (let [id, value] of postArray) {
      console.log(id, value);
      // let postPairId = value['id']
    }
   }


  return (
    <div>
      <h1 className='header'>I am the View the Market page</h1>
    </div>
  )
}


export default ViewTheMarket;
