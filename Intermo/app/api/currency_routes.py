from flask import Blueprint
from flask_login import current_user, login_required
from app.models import Currency
# from forex_python.converter import CurrencyRates

# c = CurrencyRates()
from currency_converter import CurrencyConverter
c = CurrencyConverter()


currencyRoutes = Blueprint('currency', __name__)

@currencyRoutes.route('/<base>/<quote>')
@login_required
def getCurrency(base, quote):
  id = current_user.id
  rate =  c.convert(1,f'{base}', f'{quote}')
  
  # ? keeping the below two lines, for dev purposes, to avoid hitting the database too often
  # rate = c.get_rate('EUR', 'USD')
  # rate = 1.2
  print('I am the current rate--------------', rate)

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


@currencyRoutes.route('/MarketRates')
def getMarketRates():

#todo grab all of the currency pairs from the db, split them, find the the current rate, and 24 hour change, add into a dict, send back and put into slider on the dashboard
  output = Currency.query.all()
  pairs = []
  for pair in output:
    pairArr = pair.name.split('/')
    rate = c.convert(1, pairArr[0], pairArr[1])
    pairDict = pair.to_dict()
    pairDict['rate'] = round(rate,4)
    #todo get the correct price information for today and yesterday, calculate the 24hr change, append
    pairDict['24HourChange'] = 1.2

    pairs.append(pairDict)
  print(pairs)

  # baseRates = c.get_rates(f'{base}')
  # quoteRates = c.get_rates(f'{quote}')
  return {'pairs': pairs}
