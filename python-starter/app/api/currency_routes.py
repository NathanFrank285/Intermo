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
  base = base.upper()
  quote = quote.upper()

  output = Currency.query.first().to_dict()

  # baseRates = c.get_rates(f'{base}')
  # quoteRates = c.get_rates(f'{quote}')
  return f'{output}'
