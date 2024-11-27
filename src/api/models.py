from .extensions import db

# Modelo de Usuario
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"

# Modelo de Restaurante
class RestaurantModel(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    max_capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Restaurant(name={self.name}, location={self.location})>"

# Modelo de Reservación
class ReservationModel(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    reservation_date = db.Column(db.DateTime, nullable=False)
    guests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Reservation(user_id={self.user_id}, restaurant_id={self.restaurant_id})>"
