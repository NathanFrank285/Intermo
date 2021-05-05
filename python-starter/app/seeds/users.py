# from werkzeug.security import generate_password_hash
from app.models import db, User, Currency, Trade, Post, UserBalance


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
    currency1 = Currency(name="USD")
    currency2 = Currency(name="GBP")
    currency3 = Currency(name="EUR")
    currency4 = Currency(name="CAD")
    db.session.add([currency1, currency2, currency3, currency4])
    db.session.commit()

def seed_posts():
    post = Post(userId=1, currencyId=1, price=1.5)


def seed_trades():
    trade1 = Trade(makerId=1, takerId=2, currencyId=1,
                   quantity=10, bidOrOffer="bid", created_on="5/5/2021")
    trade2 = Trade(makerId=2, takerId=1, currencyId=3,
                   quantity=10, bidOrOffer="bid", created_on="5/5/2021")
    trade3 = Trade(makerId=1, takerId=2, currencyId=4,
                   quantity=20, bidOrOffer="offer", created_on="5/5/2021")
    trade = [trade1, trade2, trade3]
    db.session.add(trade)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()

# def undo_currencies():
#     db.session.execute('TRUNCATE currencies RESTART IDENTITY CASCADE;')
#     db.session.commit()
