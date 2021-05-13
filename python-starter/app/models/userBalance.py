from .db import db


class UserBalance(db.Model):
  __tablename__ = 'userBalances'

  id = db.Column(db.Integer, primary_key=True)
  userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  currencyId = db.Column(db.Integer, db.ForeignKey(
      'fiats.id'), nullable=False)
  quantity = db.Column(db.Integer, nullable=False)
  user = db.relationship('User', back_populates='userBalance')
  userCurrencies = db.relationship('SingleCurrency', back_populates='userBalance')



  def to_dict(self):
      return {
          "id": self.id,
          "userId": self.userId,
          "currencyId": self.currencyId,
          "quantity": self.quantity,
      }
