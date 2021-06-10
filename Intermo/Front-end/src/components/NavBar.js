import React, {useState} from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector, useDispatch } from "react-redux";
import {login} from '../store/session'
import LogoutButton from './auth/LogoutButton';
import logo from '../images/Intermo-logo.png'
import './NavBar.css'

const NavBar = () => {
  const dispatch = useDispatch();
  const [email] = useState("demo@aa.io");
  const [password] = useState("password");
  const user = useSelector((state) => state?.session?.user)

  const loginDemoUser = async () => {
    return await dispatch(login(email, password));
  };


  return (
    <div className="navbar-container">
      <div className="logo">
        <NavLink to="/" exact={true} className="logo">
          <img className="logo--img" src={logo} alt="Intermo logo"></img>
        </NavLink>
      </div>
      <div className="newPost-container">
        {user ? <NavLink
          to="/newPost"
          exact={true}
          className="newPost-button authBubble"
        >
          Create an Offer
        </NavLink> : null}
      </div>
      {!user && !user ? (
        <div className="forms">
          <div className="userForms userForms--login">
            <NavLink
              to="/login"
              exact={true}
              activeClassName="active"
              className="authBubble"
            >
              Login
            </NavLink>
          </div>
          <div className="userForms userForms--login">
            <div
              activeClassName="active"
              className="authBubble"
              onClick={loginDemoUser}
            >
              Demo User
            </div>
          </div>
          <div className="userForms">
            <NavLink
              to="/sign-up"
              exact={true}
              activeClassName="active"
              className="authBubble"
            >
              Sign Up
            </NavLink>
          </div>
        </div>
      ) : (
        <div className="forms">
          <LogoutButton />
        </div>
      )}
    </div>
  );
}

export default NavBar;
