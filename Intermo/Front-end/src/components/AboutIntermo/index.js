import React from "react";
import "./AboutIntermo.css";

function AboutIntermo() {
  return (
    <div className='about-container'>
      <h2 className="header">What is Intermo?</h2>
      <div className="">Banks, on average, take a 1%-3% conversion fee just to swap from one currency to another. Intermo offers a market for individuals to avoid these fees by swapping their currencies with other users across the globe. Don't pay a middleman, use Intermo.</div>

      <h2>How to use Intermo?</h2>
      <div>Start by using the search box to find currency pair you'd want to trade. make sure that if you are buying, you have the currency on the right of the slash. If you are selling, that you own the currency to the left of the slash.

      Then, choose a quantity of currency you want to trade and hit search. Results will only show offers that are of equal quantity or more than the quantity you searched for.

      If you do not see any results, try breaking your order into smaller pieces or creating an offer so that other users can trade on your offer.
      </div>


    </div>

  );
}

export default AboutIntermo;
