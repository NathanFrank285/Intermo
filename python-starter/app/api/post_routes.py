from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import db, Currency, Post
from sqlalchemy import and_
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
  return f'{posts}'


@postRoutes.route('/', methods=['POST'])
@login_required
def postPosts():
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
