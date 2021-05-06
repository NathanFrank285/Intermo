import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from "react-redux";
import LogoutButton from './auth/LogoutButton';
import logo from '../images/Intermo-logo.png'
import './NavBar.css'

const NavBar = () => {

  const user = useSelector((state) => state?.session?.user)

  return (
    <div className="navbar-container">
      <div className="logo">
        <NavLink to="/" exact={true} activeClassName="active">
          <img className="logo--img" src={logo}></img>
        </NavLink>
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
