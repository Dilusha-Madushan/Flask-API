from flask import Flask
import sys

sys.path.append('\src\controllers')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wewqdewfrewrfew sdfgfgrefgre'

    from .prediction import prediction

    app.register_blueprint(prediction , url_prefix='/')

    return app
