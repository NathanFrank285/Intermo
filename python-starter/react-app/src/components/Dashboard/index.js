import React from "react";
import { useDispatch, useSelector } from "react-redux";
import "./Dashboard.css";

function Dashboard() {
  const user = useSelector(state => state?.session?.user)
  return (
    <div>
      {user && user ? (<h1>Hello {user.username}, welcome do your Dashboard</h1>) : (<h1>Hello, welcome to the Dashboard</h1>)}

    </div>
    // <div className="searchBar">
    //   <input type="search"></input>
    // </div>
  );
}

export default Dashboard;
