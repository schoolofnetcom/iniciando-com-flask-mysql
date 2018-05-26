from flask import Flask
from flask_marshmallow import Marshmallow
import settings
from db import db
from api.categories import categories as categories_blueprint
from api.posts import posts as posts_blueprint

app = Flask(__name__)
ma = Marshmallow(app)
    
def config_app(server):
    server.config['SERVER_NAME'] = settings.FLASK_SERVER
    server.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

def main():
    config_app(app)

    app.register_blueprint(categories_blueprint, url_prefix='/api/categories')
    app.register_blueprint(posts_blueprint, url_prefix='/api/posts')
    
    db.init_app(app)

    app.run(debug=settings.FLASK_DEBUG)

if __name__ == '__main__':
    main()
