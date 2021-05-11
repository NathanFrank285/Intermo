from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import db, Trade, Currency
from sqlalchemy import and_, or_
from forex_python.converter import CurrencyRates

c = CurrencyRates()


tradeRoutes = Blueprint('trade', __name__)

@tradeRoutes.route('')
@login_required
def getTrades():
  id = current_user.id
  trades = Trade.query.filter(or_(Trade.takerId == id, Trade.makerId == id)).all()
  output = {}
  for trade in trades:
    coin = Currency.query.filter(Currency.id == trade.makerCurrencyId).first()
    output[f'{coin.name}'] = trade.to_dict()
    # print("---------",coin.name)
  print(output)

  return output

@tradeRoutes.route('/newTrade', methods=['POST'])
@login_required
def newTrade():
  takerId = currentUserId
  #todo Delete post, then update both user balances accordingly, create new trades for each user (how to account for both sides relating to eachother, add a unique trade serial key to link offsetting sides with a uuid?)

  # todo have to inverse the direction, for taker of the trade
  if makerDirection == 'offer':
    takerDirection = 'bid'
  else:
    takerDirection = 'offer'
