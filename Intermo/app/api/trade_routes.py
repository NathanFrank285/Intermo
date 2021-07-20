from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import db, Trade, Currency, UserBalance, SingleCurrency
from sqlalchemy import and_, or_
# from forex_python.converter import CurrencyRates
from currency_converter import CurrencyConverter
c = CurrencyConverter()
import uuid
import os
# print('---------------------------',os.environ['EXCHANGE_API'])



# c = CurrencyRates('b3a198b8edb0e1f3a990f194d741fadf')


tradeRoutes = Blueprint('trade', __name__)

@tradeRoutes.route('')
@login_required
def getTrades():
  id = current_user.id
  trades = Trade.query.filter(Trade.traderId == id).all()
  output = {}
  count = 0
  for trade in trades:
    tradeDict = trade.to_dict()
    coin = Currency.query.filter(Currency.id == trade.makerCurrencyId).first()
    tradeDict['name'] = coin.name
    output[count] = tradeDict
    count += 1

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
  try:
    tradeData = request.json

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

    #! the api I was using  now requires an apikey that grants very few api calls, while I search for a new api/creating an account, I am using a single static rate for all currencies.
    # quoteQuantity = c.convert(
    #     baseQuantity, f'{baseCurrencyName}', f'{quoteCurrencyName}')
    quoteQuantity = price*baseQuantity


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
      return {'response': 'success'}
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
      return {'response': 'success'}

  except:
    return {'response': 'failed'}
