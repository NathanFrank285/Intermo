import React, { useState } from "react";
import  { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { login } from "../../store/session";
import './FormStyling.css'

const LoginForm = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data.errors) {
      setErrors(data.errors);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="container">
      <form className="form-container" onSubmit={onLogin}>
        <div >
          <div>
            {errors.map((error) => (
              <div>{error}</div>
            ))}
          </div>
          <div className="form-element">
            <h3>Please login</h3>
          </div>
          <div className="form-element">
            <label htmlFor="email">Email</label>
            <br></br>
            <input
              name="email"
              type="text"
              value={email}
              onChange={updateEmail}
              className="form-element"
            />
          </div>
          <div className="form-element">
            <label htmlFor="password">Password</label>
            <br></br>
            <input
              name="password"
              type="password"
              value={password}
              onChange={updatePassword}
              className="form-element"
            />
            <br></br>
            <button className="form-button" type="submit">
              Confirm
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
