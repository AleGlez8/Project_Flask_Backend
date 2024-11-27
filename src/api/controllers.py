from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from .models import UserModel, RestaurantModel, ReservationModel, db
from datetime import datetime

# Parsers
user_args = reqparse.RequestParser()
user_args.add_argument("username", type=str, required=True, help="Nombre de usuario es obligatorio.")
user_args.add_argument("email", type=str, required=True, help="El correo electrónico es obligatorio.")
user_args.add_argument("password", type=str, required=True, help="Contraseña obligatoria.")

restaurant_args = reqparse.RequestParser()
restaurant_args.add_argument("name", type=str, required=True)
restaurant_args.add_argument("location", type=str, required=True)
restaurant_args.add_argument("max_capacity", type=int, required=True)

reservation_args = reqparse.RequestParser()
reservation_args.add_argument("user_id", type=int, required=True)
reservation_args.add_argument("restaurant_id", type=int, required=True)
reservation_args.add_argument("reservation_date", type=str, required=True)
reservation_args.add_argument("guests", type=int, required=True)

user_fields = {"id": fields.Integer, "username": fields.String, "email": fields.String}
restaurant_fields = {"id": fields.Integer, "name": fields.String, "location": fields.String, "max_capacity": fields.Integer}
reservation_fields = {"id": fields.Integer, "user_id": fields.Integer, "restaurant_id": fields.Integer, "reservation_date": fields.String, "guests": fields.Integer}

# User Resource
class Users(Resource):
    @marshal_with(user_fields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(username=args['username'], email=args['email'], password=args['password'])
        db.session.add(user)
        db.session.commit()
        return user, 201

    def get(self):
        users = UserModel.query.all()
        return [u.username for u in users], 200

# Restaurant Resource
class Restaurants(Resource):
    @marshal_with(restaurant_fields)
    def post(self):
        args = restaurant_args.parse_args()
        restaurant = RestaurantModel(name=args['name'], location=args['location'], max_capacity=args['max_capacity'])
        db.session.add(restaurant)
        db.session.commit()
        return restaurant, 201

    def get(self):
        restaurants = RestaurantModel.query.all()
        return restaurants, 200

# Reservation Resource
class Reservations(Resource):
    @marshal_with(reservation_fields)
    def post(self):
        args = reservation_args.parse_args()
        reservation_date = datetime.strptime(args['reservation_date'], "%Y-%m-%d")
        reservation = ReservationModel(
            user_id=args['user_id'], restaurant_id=args['restaurant_id'], reservation_date=reservation_date, guests=args['guests']
        )
        db.session.add(reservation)
        db.session.commit()
        return reservation, 201
