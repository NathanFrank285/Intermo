from flask import Blueprint
from flask_login import current_user, login_required
from app.models import db, UserBalance, SingleCurrency
# from sqlalchemy import and_

userBalanceRoutes = Blueprint('userBalance', __name__)


@userBalanceRoutes.route('')
@login_required
def getUserBalance():
  id = current_user.id
  balances = UserBalance.query.filter(UserBalance.userId == id).all()
  balanceArr = []
  for balance in balances:
    balance = balance.to_dict()
    balance['currencyId'] = SingleCurrency.query.filter(SingleCurrency.id == balance['currencyId']).first().to_dict()['name']
    balanceArr.append(balance)


  return {'balances': balanceArr}
