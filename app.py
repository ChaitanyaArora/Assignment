from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from models import db, User
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
jwt = JWTManager(app)
limiter = Limiter(app, key_func=get_remote_address)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not username or not email or not password:
        return jsonify({"msg": "Missing username, email or password"}), 400

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({"msg": "Username already exists"}), 409

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201


@app.route('/login', methods=['POST'])
def login():
    # Implement login logic here

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('/secure-endpoint')
@limiter.limit("5 per minute")
def secure_endpoint():
    # Implement secure endpoint logic here

if __name__ == '__main__':
    app.run()
