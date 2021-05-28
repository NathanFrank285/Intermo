# from werkzeug.security import generate_password_hash
from app.models import db, User, Currency, Trade, Post, UserBalance, SingleCurrency


# Adds a demo user, you can add other users here if you want
def seed_users():

    demo = User(username='Demo', email='demo@aa.io',
                password='password')
    demo1 = User(username='Nathan', email='nathan@email.com',
                password='password')
    db.session.add(demo)
    db.session.add(demo1)
    db.session.commit()


def seed_currencies():
    currency1 = Currency(name="EUR/USD")
    currency2 = Currency(name="EUR/GBP")
    currency3 = Currency(name="AUD/USD")
    currency4 = Currency(name="USD/CAD")
    currency = [currency1, currency2, currency3, currency4]
    db.session.add_all(currency)
    db.session.commit()

def seed_posts():
    post = Post(userId=1, postedCurrencyId=2, wantedCurrencyId=4,
                price=1.54325, bidOrOffer='offer', created_on="5/5/2021", quantity=25, live=False)
    post1 = Post(userId=1, postedCurrencyId=1, wantedCurrencyId=2, price=1.54325, bidOrOffer='offer', created_on="5/5/2021", quantity=25, live=True)
    post2 = Post(userId=2, postedCurrencyId=1, wantedCurrencyId=3, price=1.67843,
                 bidOrOffer='offer', created_on="5/4/2021", quantity=250, live=True)
    post3 = Post(userId=1, postedCurrencyId=1, wantedCurrencyId=2, price=1.8843,
                 bidOrOffer='offer', created_on="5/4/2021", quantity=250, live=True)
    post4 = Post(userId=2, postedCurrencyId=3, wantedCurrencyId=2, price=1.67843,
                 bidOrOffer='offer', created_on="5/4/2021", quantity=250, live=True)
    post5 = Post(userId=2, postedCurrencyId=3, wantedCurrencyId=2, price=1.67843, bidOrOffer='offer', created_on="5/1/2021", quantity=250, live=False)
    posts = [post, post1, post2, post3, post4, post5]
    db.session.add_all(posts)
    db.session.commit()


def seed_trades():
    trade1 = Trade(traderId=1, makerCurrencyId=2, takerCurrencyId=1,
                   quantity=190, bidOrOffer="bid", price=1.5764, created_on="5/5/2021", postId=1, uniqueTradeId='0abeb50c-b2b7-11eb-b0c2-acde48001122')
    trade2= Trade(traderId=2, makerCurrencyId=3, takerCurrencyId=1,
                  quantity=190, bidOrOffer="offer", price=1.5764, created_on="5/5/2021", postId=1, uniqueTradeId='0abeb50c-b2b7-11eb-b0c2-acde48001123')
    trade3 = Trade(traderId=1, makerCurrencyId=2, takerCurrencyId=1,
                   quantity=510, bidOrOffer="bid", price=1.6964, created_on="5/4/2021", postId=6, uniqueTradeId='0abeb50c-b2b7-11eb-b0c2-acde48001124')
    trade = [trade1, trade2, trade3]
    db.session.add_all(trade)
    db.session.commit()

def seed_userBalance():
    balance1 = UserBalance(userId=2, currencyId=1, quantity=10000)
    balance2 = UserBalance(userId=2, currencyId=2, quantity=20000)
    balance3 = UserBalance(userId=1, currencyId=1, quantity=10000)
    balance4 = UserBalance(userId=1, currencyId=2, quantity=20000)
    balance = [balance1, balance2, balance3, balance4]
    db.session.add_all(balance)
    db.session.commit()

def seed_singleCurrencies():
    currency1 = SingleCurrency(name='EUR')
    currency2 = SingleCurrency(name='USD')
    currency3 = SingleCurrency(name='GBP')
    currency4 = SingleCurrency(name='AUD')
    currency5 = SingleCurrency(name='CAD')
    currencies = [currency1, currency2, currency3, currency4, currency5]
    db.session.add_all(currencies)
    db.session.commit()
# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()

def undo_currencies():
    db.session.execute('TRUNCATE currencies RESTART IDENTITY CASCADE;')
    db.session.commit()
def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()
def undo_trades():
    db.session.execute('TRUNCATE trades RESTART IDENTITY CASCADE;')
    db.session.commit()
def undo_userBalance():
    db.session.execute('TRUNCATE userBalances RESTART IDENTITY CASCADE;')
    db.session.commit()
def undo_singleCurrencies():
    db.session.execute('TRUNCATE fiats RESTART IDENTITY CASCADE;')
    db.session.commit()
