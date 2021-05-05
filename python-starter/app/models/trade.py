from .db import db

class Trade(db.Model):
  __tablename__ = 'trades'
  __table_args__ = (
      db.UniqueConstraint('makerId', 'takerId', 'currencyId', 'created_on', name="unique_trade"),
  )

  id = db.Column(db.Integer, primary_key=True)
  makerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  takerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  currencyId = db.Column(db.Integer, db.ForeignKey('currencies.id'), nullable=False)
  quantity = db.Column(db.Integer, nullable=False)
  # In this case bid or offer refers to whether the taker bought or sold
  bidOrOffer = db.Column(db.String(5), nullable=False)
  created_on = db.Column(db.DateTime,  default=db.func.current_timestamp(), nullable=False)
  #timestamps from Stackoverflow: https://stackoverflow.com/questions/12154129/how-can-i-automatically-populate-sqlalchemy-database-fields-flask-sqlalchemy
  maker = db.relationship('User',
                          foreign_keys=makerId)
  taker = db.relationship('User',
                          foreign_keys=takerId)


  def to_dict(self):
    return {
        "id": self.id,
        "makerId": self.makerId,
        "takerId": self.takerId,
        "currencyId": self.currencyId,
        "created_on": self.created_on,
    }
