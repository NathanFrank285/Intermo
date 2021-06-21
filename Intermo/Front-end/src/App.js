import React, { useState, useEffect } from "react";
import { useDispatch} from "react-redux";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { authenticate } from "./store/session";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar";
import Dashboard from "./components/Dashboard";
import Posts from "./components/Posts";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import NewPost from "./components/NewPost";
import Footer from "./components/Footer";
import ViewTheMarket from "./components/ViewTheMarket";
import AboutIntermo from "./components/AboutIntermo";
// import UsersList from "./components/UsersList";
// import User from "./components/User";
// import { authenticate } from "./services/auth";

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
        <Route path="/viewTheMarket" exact={true}>
          <ViewTheMarket/>
        </Route>
        <Route path="/aboutInterMo" exact={true}>
          <AboutIntermo/>
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
        <ProtectedRoute path="/newPost" exact={true}>
          <NewPost />
        </ProtectedRoute>
      </Switch>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
