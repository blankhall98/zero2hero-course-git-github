from flask import Flask

app = Flask(__name__)

def create_app():
    
    from app.main.main import main
    app.register_blueprint(main)

    return app