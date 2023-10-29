from flask_restx import Namespace, Resource, fields
from models import Review
from flask_jwt_extended import jwt_required
from flask import request

review_ns = Namespace("review", description= "A namespace for Reviews")

review_model = review_ns.model(
    "Review",
    {"id": fields.String(),"course": fields.String(), "teacher": fields.String(),
     "quality": fields.Integer(), "difficulty": fields.Integer(), "review_text": fields.String(),
      "review_date": fields.DateTime(), "reviewer_id": fields.String()}
)
@review_ns.route("/hello", methods= ["GET"])
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello World"}

@review_ns.route("/reviews", methods=["GET","POST"])
class GetReviews(Resource):
    @review_ns.marshal_list_with(review_model)
    def get(self): # Getting all Reviews
        reviews = Review.query.all()

        return reviews

    @review_ns.marshal_with(review_model)
    @review_ns.expect(review_model)
    #@jwt_required()  THIS LINE IS COMMENTED OUT BECAUSE TOKEN CREATION HAS NOT BEEN DONE
    def post(self): # Creating new Review
        
        data = request.get_json()

        new_review = Review(
            course = data.get("course") , teacher = data.get("teacher"),  quality = data.get("quality"), difficulty = data.get("difficulty"), review_text = data.get("review_text"), review_date = data.get("review_date"), reviewer_id = data.get("reviewer_id")
        )

        new_review.save()

        return new_review, 201

@review_ns.route("/course/<int:course_id>", methods=["GET"])
class GetReviews(Resource):
    def get(self, course_id):

        # Grabs Reviews by course id

        reviews = Review.query.filter_by(course= course_id).all()

        return reviews 