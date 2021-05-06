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
  for trade in trades:
    coin = Currency.query.filter(Currency.id == trade.makerCurrencyId).first()
    print(coin.currencyPair)
  print(trades)

  return "I am a new trade"
