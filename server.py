from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_session import Session
from apis import api
from config import ApplicationConfig
from models import db, User, Teacher, Review, Course


# Initializing flask app

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(ApplicationConfig)
api.init_app(app)

server_session = Session(app)
db.init_app(app)


with app.app_context():
    db.create_all()


''''
@app.route("/<int:id>", methods= ["GET"])
def details()
'''


# Running app
if __name__ == '__main__':
    app.run(debug=True)


