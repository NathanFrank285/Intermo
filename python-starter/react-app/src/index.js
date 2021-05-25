import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import './index.css';
import App from './App';
import configureStore from './store'
import ReactNotification from "react-notifications-component";
import "react-notifications-component/dist/theme.css";


const store = configureStore();

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <div className="app-container">
        <ReactNotification/>
        <App />
      </div>
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
