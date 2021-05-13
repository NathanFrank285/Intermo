from flask import Blueprint
from flask_login import current_user, login_required
from app.models import db, Currency, Post, User
from sqlalchemy import and_
from forex_python.converter import CurrencyRates

c = CurrencyRates()


postRoutes = Blueprint('post', __name__)

@postRoutes.route('/<base>/<quote>/<quantity>/<direction>')
@login_required
def getPosts(base, quote, quantity, direction):
  id = current_user.id
  # pairId = Currency.query.filter(Currency.id == base).first().to_dict()

  # Grab the pair that matches the search
  pairName = Currency.query.filter(and_(Currency.name.startswith(base), Currency.name.endswith(quote))).first().to_dict()

  #search for all posts that match the currency pair, opposite direction of the search, and are greater than or equal to the searched quantity
  posts = Post.query.filter(and_(Post.postedCurrencyId == pairName['id']), Post.bidOrOffer != direction, Post.quantity >= quantity, Post.userId != id).join(User).all()
  # todo the user object is being added to the posts variable, need to find a way to add this to the dict function so it can be sent to redux

  output = {}
  count = 0
  for post in posts:
    postDict = post.to_dict()
    postDict['name'] = pairName['name']
    output[count] = postDict
    count += 1
  # output['search'] = [base, quantity, direction]

  return output


@postRoutes.route('/', methods=['POST'])
@login_required
def postPosts():
  post = Post.query.filter(Post.userId == id).first()

  db.session.add()
  db.session.commit()
  # use the request object from flask to access the body of post request

  return


@postRoutes.route('/<postId>', methods=['DELETE'])
@login_required
def deletePosts(postId):
  id = current_user.id
  post = Post.query.filter(and_(Post.userId == id, Post.id == postId)).first()
  db.session.delete(post)
  db.session.commit()
  return 'success'


@postRoutes.route('/<postId>', methods=['PUT'])
@login_required
def putPosts(postId):
  id = current_user.id
  post = Post.query.filter(and_(Post.userId == id, Post.id == postId)).first().to_dict()

  return
