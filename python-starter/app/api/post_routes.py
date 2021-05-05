from flask import Blueprint
from flask_login import current_user, login_required
from app.models import Currency, Post
from forex_python.converter import CurrencyRates

c = CurrencyRates()


postRoutes = Blueprint('post', __name__)

@postRoutes.route('/')
@login_required
def getPosts():
  id = current_user.id
  posts = Post.query.filter(Post.userId == id).all()
  posts = [post.to_dict() for post in posts]
  print(posts)
  return f'{id}'


@postRoutes.route('/', methods=['POST'])
@login_required
def getPosts():
  return


@postRoutes.route('/', methods=['DELETE'])
@login_required
def getPosts():
  
  return 'success'

@postRoutes.route('/', methods=['PUT'])
@login_required
def getPosts():
  return
