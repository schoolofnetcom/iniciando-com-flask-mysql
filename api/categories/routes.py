from . import categories
from flask import request, jsonify
from db import db
from marshmallow import Schema, fields
from db.models import Category

class CategorySchema(Schema):
    class Meta:
        fields = ( 'id', 'name' )

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

@categories.route('/', methods=['GET'])
def list():
    all_categories = Category.query.all()
    res = categories_schema.dump(all_categories)

    return jsonify(res.data)

@categories.route('', methods=['POST'])
def create():
    name = request.json['name']

    new_category = Category(name)

    db.session.add(new_category)
    db.session.commit()

    return jsonify(id = new_category.id, name = new_category.name)

@categories.route('/<id>', methods=['PUT'])
def update(id):
    category = Category.query.get(id)

    name = request.json['name']
    category.name = name

    db.session.commit()

    return category_schema.jsonify(category)

@categories.route('/<id>', methods=['DELETE'])
def remove(id):
    category = Category.query.get(id)

    db.session.delete(category)
    db.session.commit()

    return category_schema.jsonify(category)
