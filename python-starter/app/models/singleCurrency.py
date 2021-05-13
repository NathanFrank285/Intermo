from .db import db

class SingleCurrency(db.Model):
  __tablename__ = 'fiats'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(3), nullable=False, unique=True)


  userBalance = db.relationship('UserBalance', back_populates='userCurrencies')

  def to_dict(self):
    return {
        "id": self.id,
        "name": self.name
    }
