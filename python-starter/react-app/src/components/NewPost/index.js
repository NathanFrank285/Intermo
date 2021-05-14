import React,{useState, useEffect}  from "react";
import { useDispatch } from "react-redux";
import {newPostThunk} from '../../store/posts'
import "./NewPost.css";


function NewPost() {
  const dispatch = useDispatch();
  const [pair, setPairSearchValue] = useState("EUR/USD");
  const [quantity, setQuantity] = useState("");
  const [direction, setDirection] = useState("bid");

  const onSubmit = () => {
    const data = {

    }
    dispatch(newPostThunk(data))
  }

  return (
    <div className="newPost-Container">
      <form onSubmit={onSubmit}>
        <label>Do you want to buy or sell?</label>
        <select onChange={(e)=>setDirection(e.target.value)} className="">
          <option value="bid">Buy</option>
          <option value="offer">Sell</option>
        </select>
      </form>
    </div>
  )
}

export default NewPost;
