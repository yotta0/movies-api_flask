from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'jlkjjlkjsalkdjlks'
    app.config.from_pyfile('config.py')

    from .views import views

    app.register_blueprint(views, url_prefix='/')
    return app