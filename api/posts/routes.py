from . import posts
from flask import request, jsonify
from db import db
from marshmallow_sqlalchemy import ModelSchema
from db.models import Post
from db.models import Category

class PostSchema(ModelSchema):
    class Meta:
        model = Post

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

@posts.route('/', methods=['GET'])
def list():
    all_posts = Post.query.all()
    res = posts_schema.dump(all_posts).data

    return jsonify(res)

@posts.route('', methods=['POST'])
def create():
    title = request.json['title']
    body = request.json['body']
    category_id = request.json['category_id']

    category = Category.query.get(category_id)

    new_post = Post(title, body, category)

    db.session.add(new_post)
    db.session.commit()

    res = post_schema.dump(new_post).data

    return jsonify(res)

@posts.route('/<int:id>', methods=['DELETE'])
def remove(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()

    return '', 204