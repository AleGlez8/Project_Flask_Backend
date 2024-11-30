from datetime import datetime
import unittest
from unittest.mock import patch
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from src.app import app, db

class TestRestaurantReservationSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        cls.client = app.test_client()
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # --- USER TESTS ---
    def test_create_user(self):
        response = self.client.post('/api/users', json={
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password': 'securepassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_get_users(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_user_by_id(self):
        response = self.client.get('/api/users/1')
        if response.status_code == 404:
            self.skipTest("User with ID 1 does not exist yet.")
        self.assertEqual(response.status_code, 200)
        self.assertIn('email', response.json)

    def test_update_user(self):
        self.client.post('/api/users', json={
            'name': 'Old Name',
            'email': 'oldemail@example.com',
            'password': 'oldpassword'
        })
        response = self.client.put('/api/users/1', json={
            'name': 'Updated Name',
            'email': 'updatedemail@example.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Updated Name')

    def test_delete_user(self):
        response = self.client.delete('/api/users/1')
        self.assertIn(response.status_code, [204, 404])

    # --- RESTAURANT TESTS ---
    def test_create_restaurant(self):
        response = self.client.post('/api/restaurants', json={
            'name': 'Test Restaurant',
            'address': '123 Test St',
            'phone': '1234567890'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_get_restaurants(self):
        response = self.client.get('/api/restaurants')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    # --- RESERVATION TESTS ---
    def test_create_reservation(self):
        self.client.post('/api/users', json={
            'name': 'Test User',
            'email': 'testuser2@example.com',
            'password': 'password2'
        })
        self.client.post('/api/restaurants', json={
            'name': 'Another Restaurant',
            'address': '456 Another St',
            'phone': '0987654321'
        })
        response = self.client.post('/api/reservations', json={
            'user_id': 1,
            'restaurant_id': 1,
            'reservation_date': '2024-12-31T20:00:00',
            'number_of_people': 4
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_get_reservations(self):
        response = self.client.get('/api/reservations')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_delete_reservation(self):
        response = self.client.delete('/api/reservations/1')
        self.assertIn(response.status_code, [204, 404])

if __name__ == '__main__':
    unittest.main()
