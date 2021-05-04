from .db import db


class Currency(db.Model):
  __tablename__ = 'currencies'

  id = db.Column(db.Integer, primary_key=True)
  currencyPair = db.Column(db.String(15), nullable = False, unique = True)
  user = db.relationship('User', back_populates='userCurrencies')

  def to_dict(self):
    return {
        "id": self.id,
        "currencyPair": self.currencyPair
    }
