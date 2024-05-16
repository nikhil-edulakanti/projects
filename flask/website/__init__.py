from flask import Flask,app
from flask_sqlalchemy import SQLAlchemy
from os import path 
from flask_login import LoginManager



db=SQLAlchemy()
DB_NAME="database.db"

def create_app():
    app=Flask(__name__)
    app.config["SECRET_KEY"]="qwerty"
    app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{DB_NAME}"
    db.init_app(app)
    

    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/auth")
     

    login_manager=LoginManager()
    login_manager.login_view="auth.login"
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        from .models import User, Note
        return User.query.get(int(id))
    
    
    
    with app.app_context():
        create_database()
    
    

    return app

def create_database( ):
    if not path.exists("website/"+ DB_NAME):
        db.create_all()
        print("DATABASE CREATED")