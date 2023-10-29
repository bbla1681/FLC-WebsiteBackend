from flask_restx import Namespace, Resource, fields
from models import db , User
from flask import Response,Flask, request, jsonify, json, session
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session



auth_ns = Namespace("auth", description= "A namespace for authentication")
auth_model = auth_ns.model(
    "User",
    {"id": fields.String(), "email": fields.String(), "password": fields.String() }
)


@auth_ns.route("/register", methods=["POST"])
class RegisterUser(Resource):
    @auth_ns.expect(auth_model)
    def post(self):
        data = request.get_json()
        
        email = data.get("email")

        user_exists = User.query.filter_by(email=email).first()

        if user_exists:
            return jsonify({"error": "User already exists"})

        hashed_password = generate_password_hash(data.get("password"))
        new_user = User(email=email, password=hashed_password)

        new_user.save()

        user_dict = {"id": new_user.id, "email": new_user.email}


        return user_dict, 201

@auth_ns.route("/login", methods=["POST"])        
class LoginUser(Resource):    
    @auth_ns.expect(auth_model)
    def post(self):
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()

        if user is None:
            return jsonify({"message": "Invalid username or password"})
        if not check_password_hash(user.password, password):
            return jsonify({"message": "Invalid username or password"})
        
        user_dict = {"id": user.id, "email": user.email}
        jsonify(user_dict)
        session["user_id"] = user.id

        
        return user_dict, 201
