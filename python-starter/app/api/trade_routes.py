from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import db, Trade, Currency, UserBalance, SingleCurrency
from sqlalchemy import and_, or_
from forex_python.converter import CurrencyRates
import uuid


c = CurrencyRates()


tradeRoutes = Blueprint('trade', __name__)

@tradeRoutes.route('')
@login_required
def getTrades():
  id = current_user.id
  trades = Trade.query.filter(Trade.traderId == id).all()
  print("---------------TRADES",trades)
  output = {}
  count = 0
  for trade in trades:
    tradeDict = trade.to_dict()
    coin = Currency.query.filter(Currency.id == trade.makerCurrencyId).first()
    tradeDict['name'] = coin.name
    print(tradeDict['name'])
    output[count] = tradeDict
    count += 1
    # print("---------",coin.name)
  print(output)

  return output


# {
# 'date': '2021-05-11T22:33:19.532Z',
# 'postedCurrencyId': 1
# 'makerDirection': 'offer',
#  'price': 1.54325,
# 'quantity': 25,
# 'makerId': 1,
# 'postId': 1,
# 'tradeQuantity': 5
# }

@tradeRoutes.route('/newTrade', methods=['POST'])
@login_required
def newTrade():
  tradeData = request.json


  # todo use the converted quantity to adjust user balances correctly, 1.2 USD per 1 etc. need to get the converted amount and use the tradeQuantity and the converted quantity from the api to add and subtract the correct amounts from both balances on each user
  # rate = c.get_rate('USD', 'INR')
  # convertedQuantity = c.convert('USD', 'INR', 10)
  # print(rate, "--------------------I am the RATEEEEE")


  #? Trade ingredients
  makerId = tradeData['makerId']
  takerId = current_user.id

  makerCurrencyId = tradeData['postedCurrencyId']
  takerCurrencyId = tradeData['postedCurrencyId']

  quantity = tradeData['quantity']
  makerDirection = tradeData['makerDirection']
  price = tradeData['price']
  postId = tradeData['postId']
  baseQuantity = tradeData['tradeQuantity']
  date = tradeData['date']

  baseCurrencyId = SingleCurrency.query.filter(
      SingleCurrency.name == tradeData['baseName']).first().to_dict()['id']
  baseCurrencyName = tradeData['baseName']
  quoteCurrencyId = SingleCurrency.query.filter(
      SingleCurrency.name == tradeData['quoteName']).first().to_dict()['id']
  quoteCurrencyName = tradeData['quoteName']
  quoteQuantity = c.convert(
      f'{baseCurrencyName}', f'{quoteCurrencyName}', baseQuantity)

  uniqueTradeId = uuid.uuid1()




  if makerDirection == 'offer':
    takerDirection = 'bid'
    #Subtract trade quantity from the balance of maker
    makerBaseBalance = UserBalance.query.filter(and_(
        UserBalance.userId == makerId, UserBalance.currencyId == baseCurrencyId)).first()

    makerQuoteBalance = UserBalance.query.filter(and_(
        UserBalance.userId == makerId, UserBalance.currencyId == quoteCurrencyId)).first()

    makerBaseBalance.quantity = makerBaseBalance.quantity - baseQuantity
    makerQuoteBalance.quantity = makerQuoteBalance.quantity + quoteQuantity
    #Add trade quantity to the balance of taker
    takerBaseBalance = UserBalance.query.filter(and_(
        UserBalance.userId == takerId, UserBalance.currencyId == baseCurrencyId)).first()

    takerQuoteBalance = UserBalance.query.filter(and_(UserBalance.userId == takerId, UserBalance.currencyId == quoteCurrencyId)).first()

    takerBaseBalance.quantity = takerBaseBalance.quantity + baseQuantity
    takerQuoteBalance.quantity = takerQuoteBalance.quantity - quoteQuantity
    # commit both changes to the user Balance
    db.session.commit()

    #Create new trades for both the maker and taker
    makerTrade = Trade(
      makerCurrencyId=makerCurrencyId,
      takerCurrencyId=takerCurrencyId,
      quantity=quoteQuantity,
      bidOrOffer=makerDirection,
      price=price,
      postId=postId,
      created_on=date,
      traderId = makerId,
      uniqueTradeId=uniqueTradeId
    )

    takerTrade = Trade(
      makerCurrencyId=makerCurrencyId,
      takerCurrencyId=takerCurrencyId,
      quantity=baseQuantity,
      bidOrOffer=takerDirection,
      price=price,
      postId=postId,
      created_on=date,
      traderId = takerId,
      uniqueTradeId=uniqueTradeId
    )
    db.session.add_all([makerTrade, takerTrade])
    db.session.commit()

  else:
    takerDirection = 'offer'

    #Subtract trade quantity from the balance of maker
    makerBaseBalance = UserBalance.query.filter(and_(
        UserBalance.userId == makerId, UserBalance.currencyId == baseCurrencyId)).first()

    makerQuoteBalance = UserBalance.query.filter(and_(
        UserBalance.userId == makerId, UserBalance.currencyId == quoteCurrencyId)).first()

    makerBaseBalance.quantity = makerBaseBalance.quantity + baseQuantity
    makerQuoteBalance.quantity = makerQuoteBalance.quantity - quoteQuantity
    #Add trade quantity to the balance of taker
    takerBaseBalance = UserBalance.query.filter(and_(
        UserBalance.userId == takerId, UserBalance.currencyId == baseCurrencyId)).first()

    takerQuoteBalance = UserBalance.query.filter(and_(
        UserBalance.userId == takerId, UserBalance.currencyId == quoteCurrencyId)).first()

    takerBaseBalance.quantity = takerBaseBalance.quantity - baseQuantity
    takerQuoteBalance.quantity = takerQuoteBalance.quantity + quoteQuantity
    # commit both changes to the user Balance
    db.session.commit()

    #Create new trades for both the maker and taker
    makerTrade = Trade(
        makerCurrencyId=makerCurrencyId,
        takerCurrencyId=takerCurrencyId,
        quantity=baseQuantity,
        bidOrOffer=makerDirection,
        price=price,
        postId=postId,
        created_on=date,
        traderId=makerId,
        uniqueTradeId=uniqueTradeId
    )

    takerTrade = Trade(
        makerCurrencyId=makerCurrencyId,
        takerCurrencyId=takerCurrencyId,
        quantity=baseQuantity,
        bidOrOffer=takerDirection,
        price=price,
        postId=postId,
        created_on=date,
        traderId=takerId,
        uniqueTradeId=uniqueTradeId
    )
    db.session.add_all([makerTrade, takerTrade])
    db.session.commit()






  return {'success': ''}


  #todo  create new trades for each user (how to account for both sides relating to eachother, add a unique trade serial key to link offsetting sides with a uuid?), check if the total quantity would put the Posters desired trade value to 0, if so, set the Post.live to False, else leave it true

  # todo have to inverse the direction, for taker of the trade
