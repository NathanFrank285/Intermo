from .db import db


class Post(db.Model):
    __tablename__ = 'posts'
    __table_args__ = (
        db.UniqueConstraint('userId', 'postedCurrencyId','wantedCurrencyId', 'price', 'bidOrOffer', 'created_on', 'updated_on','quantity', name="unique_post"),
    )

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    postedCurrencyId = db.Column(db.Integer, db.ForeignKey(
        'currencies.id'), nullable=False)
    wantedCurrencyId = db.Column(db.Integer, db.ForeignKey(
        'currencies.id'), nullable=False)
    price = db.Column(db.Float(6), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    bidOrOffer = db.Column(db.String(5), nullable=False)
    created_on = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_on = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    # timestamps from Stackoverflow: https://stackoverflow.com/questions/12154129/how-can-i-automatically-populate-sqlalchemy-database-fields-flask-sqlalchemy
    user = db.relationship('User', back_populates='userPosts')
    postedCurrency = db.relationship('Currency',
                                       foreign_keys=postedCurrencyId)
    wantedCurrency = db.relationship('Currency',
                                       foreign_keys=wantedCurrencyId)

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "postedCurrencyId": self.postedCurrencyId,
            "wantedCurrencyId": self.wantedCurrencyId,
            "price": self.price,
            "bidOrOffer": self.bidOrOffer,
            "quantity": self.quantity,
            "created_on": self.created_on,
            "updated_on": self.updated_on,
        }
