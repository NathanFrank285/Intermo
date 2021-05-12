import {createStore, combineReducers, applyMiddleware, compose } from "redux";
import thunk from 'redux-thunk';
import session from './session'
import posts from './posts';
import trades from './trades'
import pairs from './pairs'
import userBalance from './userBalance'
import search from './search'
import currentRate from './currentRate'



const rootReducer = combineReducers({
    session,
    posts,
    trades,
    pairs,
    userBalance,
    search,
    currentRate,

});

let enhancer;

if (process.env.NODE_ENV === 'production') {
    enhancer = applyMiddleware(thunk);
} else {
    const logger = require('redux-logger').default;
    const composeEnhancers =
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
    enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
    return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
