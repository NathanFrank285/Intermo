from .db import db


class Currency(db.Model):
  __tablename__ = 'currencies'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(15), nullable = False, unique = True)
  userBalance = db.relationship('UserBalance', back_populates='userCurrencies')

  makerCurrency = db.relationship(
      'Trade', back_populates='makerCurrency', foreign_keys='Trade.makerCurrencyId')
  takerCurrency = db.relationship(
      'Trade', back_populates='takerCurrency', foreign_keys='Trade.takerCurrencyId')
  postedCurrency = db.relationship(
      'Post', back_populates='postedCurrency', foreign_keys='Post.postedCurrencyId')
  wantedCurrency = db.relationship(
      'Post', back_populates='wantedCurrency', foreign_keys='Post.wantedCurrencyId')

  def to_dict(self):
    return {
        "id": self.id,
        "currencyPair": self.currencyPair
    }
