import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, NavLink } from "react-router-dom";
import ExchangeRates from '../ExchangeRates'
import SinglePost from "../SinglePost";
import {newTradeThunk} from '../../store/trades'
import { store } from "react-notifications-component";

// import { getUserBalanceThunk } from "../../store/userBalance";
import "./Posts.css";

function Posts() {
  const dispatch = useDispatch();
  let posts = useSelector(state=>state?.posts)
  let tradeQuantity = useSelector(state=>Number(state?.search?.quantity))
  let baseName = useSelector((state) => state?.search?.base);
  let quoteName = useSelector((state) => state?.search?.quote);
  const history = useHistory();
  // const [makerId, setMakerId] = useState(0)
  // const [makerCurrencyId, setMakerCurrencyId] = useState(0)
  // const [quantity, setQuantity] = useState(0)
  // const [price, setPrice] = useState(0)
  // const [makerDirection, setMakerDirection] = useState('offer')


  let numberOfPosts;

  if (posts) {
    numberOfPosts = Object.entries(posts).length
    posts = Object.entries(posts)
  }

const submitTrade = async (date, postedCurrencyId, makerDirection, price, quantity, makerId, postId) => {
  const data = {
    date,
    postedCurrencyId,
    makerDirection,
    price,
    quantity,
    makerId,
    postId,
    tradeQuantity,
    baseName,
    quoteName
  };

  const {response} = await dispatch(newTradeThunk(data))

  if (response === 'success') {
      store.addNotification({
        title: "Trade Complete!",
        message: "Success, your trade is confirmed",
        type: "success",
        insert: "bottom",
        container: "bottom-right",
        animationIn: ["animate__animated", "animate__fadeIn"],
        animationOut: ["animate__animated", "animate__fadeOut"],
        dismiss: {
          duration: 5000,
          onScreen: true,
        }
      });
      history.push("/");
    } else {
      store.addNotification({
        title: "Trade unsuccesful",
        message: "Please check you have enough funds and try again",
        type: "danger",
        insert: "bottom",
        container: "bottom-right",
        animationIn: ["animate__animated", "animate__fadeIn"],
        animationOut: ["animate__animated", "animate__fadeOut"],
        dismiss: {
          duration: 5000,
          onScreen: true,
        }
      })
      history.push('/')

}}

    return (
      <div>
        <SinglePost/>
        <div className="currentRate">
          <ExchangeRates/>
        </div>
        <div className="postContainer">
          {numberOfPosts > 0 ? (
            posts.map((post, id) => {

              let date = new Date(
                post[1].created_on
              ).toLocaleDateString();
              return (
                <div key={id} className="singlePost">
                  <div className="postElement">{post[1].name}</div>
                  <div className="postElement">Posted on {date}</div>
                  <div className="postElement">
                    {post[1].bidOrOffer.charAt().toUpperCase() +
                      post[1].bidOrOffer.slice(1)}{" "}
                    is at {post[1].price}
                  </div>
                  <div className="postElement">
                    Quantity: {post[1].quantity}
                  </div>
                  <button
                    className="tradeButton form-button"
                    onClick={() => {
                      submitTrade(
                        new Date(),
                        post[1].postedCurrencyId,
                        post[1].bidOrOffer,
                        post[1].price,
                        post[1].quantity,
                        post[1].userId,
                        post[1].id
                      );
                    }}
                  >
                    Trade
                  </button>
                </div>
              );})
          ) : (
            <NavLink to='/'>
              <div>No trade offers available, try searching for a lower quantity or creating an offer</div>
            </NavLink>
          )}
        </div>
      </div>
    );
}

export default Posts;
