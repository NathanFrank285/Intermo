from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import db, Trade, Currency, UserBalance
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

  #? Trade ingredients
  print(tradeData)
  makerId = tradeData['makerId']
  takerId = current_user.id
  makerCurrencyId = tradeData['postedCurrencyId']
  quantity = tradeData['quantity']
  makerDirection = tradeData['makerDirection']
  price = tradeData['price']
  postId = tradeData['postId']
  tradeQuantity = tradeData['tradeQuantity']
  date = tradeData['date']
  uniqueTradeId = uuid.uuid1()

  if makerDirection == 'offer':
    takerDirection = 'bid'
    #Subtract trade quantity from the balance of maker
    makerBalance = UserBalance.query.filter(and_(UserBalance.userId == makerId, UserBalance.currencyId == makerCurrencyId)).first()
    makerBalance.quantity = makerBalance.quantity - tradeQuantity

    #Add trade quantity to the balance of taker
    takerBalance = UserBalance.query.filter(and_(UserBalance.userId == takerId, UserBalance.currencyId == makerCurrencyId)).first()
    takerBalance.quantity = takerBalance.quantity + tradeQuantity
    # commit both changes to the user Balance
    db.session.commit()
    #Create new trades for both the maker and taker
    # makerTrade = Trade(

    #   quantity=tradeQuantity,
    #   bidOrOffer=makerDirection,
    #   price=price,
    #   postId=postId,
    #   created_on=date,
    #   traderId = makerId,
    #   uniqueTradeId=uniqueTradeId
    # )



  else:
    takerDirection = 'offer'






  return {'success': 'sucks'}


  #todo  create new trades for each user (how to account for both sides relating to eachother, add a unique trade serial key to link offsetting sides with a uuid?), check if the total quantity would put the Posters desired trade value to 0, if so, set the Post.live to False, else leave it true

  # todo have to inverse the direction, for taker of the trade
