import React, { useState, useEffect } from "react";
import { useDispatch} from "react-redux";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar";
import Dashboard from "./components/Dashboard";
import Posts from "./components/Posts";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
// import { authenticate } from "./services/auth";
import { authenticate } from "./store/session";

function App() {
  // const [authenticated, setAuthenticated] = useState(false);
  const dispatch = useDispatch()
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async() => {
      await dispatch(authenticate())
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        {/* <ProtectedRoute path="/users" exact={true} >
          <UsersList/>
        </ProtectedRoute> */}
        {/* <ProtectedRoute path="/users/:userId" exact={true} >
          <User />
        </ProtectedRoute> */}
        <Route path="/" exact={true}>
          <Dashboard />
        </Route>
        <ProtectedRoute path="/posts" exact={true}>
          <Posts />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
