# Front end routes

## /homepage
### Logged in
  * GET /homepage
    ** for account holders only, shows balances and historical trades

## /search
  * GET /currencies
    *  after user searches for a currency pair, will show the results that user can tehn select

## /quotes
  * GET /Quotes
    * All of the available offers to exchange your currency

# Back end routes

## /posts
  * GET /posts/<direction>/<pair>
    * return all of the posts that match a certain currency pair and direction
  * POST /posts/<pair>
    * create a new post for users to trade with

  * DELETE /posts/<pair>
    * delete a post a user had made

  ###optional
  * PUT /posts/<pair>
    * edit post that a user had made

## /trade
  * GET /conversions
    * Get a list of all conversions a user had done

  * POST /trade
    * post a new conversion
