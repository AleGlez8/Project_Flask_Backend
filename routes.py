from flask import request, jsonify
from models import products, Product
from auth import auth

def configure_routes(app):
    @app.route('/products', methods=['GET'])
    def get_products():
        result = [{'id': p.id, 'name': p.name, 'price': p.price, 'stock': p.stock} for p in products]
        return jsonify(result)

    @app.route('/products/<int:product_id>', methods=['GET'])
    def get_product(product_id):
        product = next((p for p in products if p.id == product_id), None)
        if product:
            return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'stock': product.stock})
        return jsonify({'error': 'Product not found'}), 404

    @app.route('/products', methods=['POST'])
    @auth.login_required
    def add_product():
        new_product = request.json
        product = Product(len(products) + 1, new_product['name'], new_product['price'], new_product['stock'])
        products.append(product)
        return jsonify({'id': product.id}), 201
