from .db import db

class Trade(db.Model):
  __tablename__ = 'trades'
  __table_args__ = (
      db.UniqueConstraint('traderId', 'makerCurrencyId', 'takerCurrencyId','quantity','bidOrOffer','price', 'created_on', name="unique_trade"),
  )

  id = db.Column(db.Integer, primary_key=True)
  traderId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  makerCurrencyId = db.Column(
      db.Integer, db.ForeignKey('currencies.id'), nullable=False)
  takerCurrencyId = db.Column(
      db.Integer, db.ForeignKey('currencies.id'), nullable=False)

  quantity = db.Column(db.Integer, nullable=False)
  # In this case bid or offer refers to whether the taker bought or sold
  bidOrOffer = db.Column(db.String(5), nullable=False)
  price = db.Column(db.Float(6), nullable=False)
  postId = db.Column(db.Integer, db.ForeignKey(
      'posts.id'), nullable=False)
  uniqueTradeId = db.Column(db.String(36), nullable=False, unique=True)
  created_on = db.Column(db.DateTime,  default=db.func.current_timestamp(), nullable=False)
  #timestamps from Stackoverflow: https://stackoverflow.com/questions/12154129/how-can-i-automatically-populate-sqlalchemy-database-fields-flask-sqlalchemy
  post = db.relationship('Post', back_populates='trades')
  trader = db.relationship('User',
                          back_populates='trades')

  makerCurrency = db.relationship('Currency',
                                  foreign_keys=makerCurrencyId)
  takerCurrency = db.relationship('Currency',
                                  foreign_keys=takerCurrencyId)

  def to_dict(self):
    return {
        "id": self.id,
        "traderId": self.traderId,
        "makerCurrencyId": self.makerCurrencyId,
        "takerCurrencyId": self.takerCurrencyId,
        "quantity": self.quantity,
        "bidOrOffer": self.bidOrOffer,
        "price": self.price,
        "created_on": self.created_on,
    }
