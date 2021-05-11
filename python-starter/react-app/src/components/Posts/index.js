import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
// import { NavLink, useHistory } from "react-router-dom";
// import {getPostsThunk} from '../../store/posts'
import "./Posts.css";

function Posts() {
  const dispatch = useDispatch();
  let posts = useSelector(state=>state?.posts)
  let numberOfPosts;
  if (posts) {
    numberOfPosts = Object.entries(posts).length
    posts = Object.entries(posts)
  }
  console.log(posts);
// bidOrOffer: "offer";
// created_on: "Wed, 05 May 2021 00:00:00 GMT";
// id: 1;
// postedCurrencyId: 1;
// price: 1.54325;
// quantity: 25;
// updated_on: "Wed, 05 May 2021 16:50:33 GMT";
// userId: 1;
// wantedCurrencyId: 2;
//todo create a seperate store for search data so this can be accessed
    return(
    <div className="postsContainer">
      {(numberOfPosts > 0)
        ? posts.map((post)=>(
          <div className="singlePost">
            <div>{post[1].created_on}</div>

          </div>
        ))
        : <div>False</div>}
    </div>
    )

  ;
}

export default Posts;
