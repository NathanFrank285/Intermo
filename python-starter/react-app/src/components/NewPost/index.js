import React,{useState, useEffect}  from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import {newPostThunk} from '../../store/posts'
import { getCurrenciesThunk } from "../../store/pairs";
import "./NewPost.css";


function NewPost() {
  const dispatch = useDispatch();
  const history = useHistory()
  const pairs = useSelector((state) => state?.pairs[0]);
  const [pair, setPairSearchValue] = useState('1');
  const [quantity, setQuantity] = useState("");
  const [price, setPrice] = useState("");
  const [direction, setDirection] = useState("bid");

  useEffect(() => {
    dispatch(getCurrenciesThunk());
    // eslint-disable-next-line
  }, []);

  const submitPost = (e) => {
    e.preventDefault();
    const data = {
      pair,
      quantity,
      price,
      direction
    }

    dispatch(newPostThunk(data))
    history.push("/");
  }

  return (
    <>
      <div>Current exchange rate is: </div>
      <div className="newPost-Container">
        <form className="form-container" onSubmit={(e) => submitPost(e)}>
        <h3>Create a new Post!</h3>
          <label>What currency pair do you want to post?</label>
          <select required onChange={(e) => setPairSearchValue(e.target.value)}>
            {pairs &&
              pairs.map((pair) => (
                <option key={pair["id"]} value={pair["id"]}>
                  {pair["name"]}
                </option>
              ))}
          </select>
          <br></br>
          <label>Do you want to buy or sell?</label>
          <select
            onChange={(e) => setDirection(e.target.value)}
            className="form-element"
          >
            <option value="bid">Buy</option>
            <option value="offer">Sell</option>
          </select>
          <br></br>
          {direction === "bid" ? (
            <label>How much do you want to buy?</label>
          ) : (
            <label>How much do you want to sell?</label>
          )}
          <input
            required
            type="number"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
            className="form-element"
          ></input>
          <br></br>
          {direction === "bid" ? (
            <label>What price do you want to buy at?</label>
          ) : (
            <label>What price do you want to sell at?</label>
          )}

          <input
            required
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            className="form-element"
          ></input>
          <br></br>
          <button className="form-button" type="submit">
            Post
          </button>
        </form>
      </div>
    </>
  );
}

export default NewPost;
