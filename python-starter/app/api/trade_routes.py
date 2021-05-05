from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import db, Trade
from sqlalchemy import and_, or_
from forex_python.converter import CurrencyRates

c = CurrencyRates()


tradeRoutes = Blueprint('trade', __name__)

@tradeRoutes.route('')
@login_required
def getTrades():
  id = current_user.id
  trades = Trade.query.filter(or_(Trade.takerId == id, Trade.makerId == id)).all().to_dict()
  print(trades)

  return "I am a new trade"
