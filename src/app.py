from flask import Flask
from flask_restful import Api
from api.extensions import db
from api.controllers import Users, Restaurants, Reservations

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db.init_app(app)

api.add_resource(Users, "/api/users")
api.add_resource(Restaurants, "/api/restaurants")
api.add_resource(Reservations, "/api/reservations")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
