from flask import Blueprint
from flask_login import current_user, login_required
from app.models import Currency
from forex_python.converter import CurrencyRates

c = CurrencyRates()


currencyRoutes = Blueprint('currency', __name__)

@currencyRoutes.route('/<base>/<quote>')
@login_required
def getCurrency(base, quote):
  id = current_user.id
  # rate =  c.get_rate(f'{base}', f'{quote}')
  rate = c.get_rate('EUR', 'USD')

  return {'rate': rate}

@currencyRoutes.route('')
def getCurrencies():

  output = Currency.query.all()
  pairs = []
  for pair in output:
    pairs.append(pair.to_dict())

  # baseRates = c.get_rates(f'{base}')
  # quoteRates = c.get_rates(f'{quote}')
  return {'pairs': pairs}
