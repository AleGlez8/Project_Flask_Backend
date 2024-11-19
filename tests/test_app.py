import pytest
from app import app
from base64 import b64encode

@pytest.fixture
def client():
    # Configura la aplicación para el modo de prueba
    app.config['TESTING'] = True
    # Crea un cliente de prueba para la aplicación
    with app.test_client() as client:
        yield client

def test_get_products(client):
    # Prueba la obtención de todos los productos
    rv = client.get('/products')
    assert rv.status_code == 200  # Verifica que el estado de la respuesta sea 200 (OK)
    assert len(rv.get_json()) == 3  # Verifica que haya 3 productos en la respuesta

def test_get_product(client):
    # Prueba la obtención de un producto específico por ID
    rv = client.get('/products/1')
    assert rv.status_code == 200  # Verifica que el estado de la respuesta sea 200 (OK)
    assert rv.get_json()['name'] == 'Collar'  # Verifica que el nombre del producto sea 'Collar'

def test_get_nonexistent_product(client):
    # Prueba la obtención de un producto que no existe
    rv = client.get('/products/999')
    assert rv.status_code == 404  # Verifica que el estado de la respuesta sea 404 (No encontrado)

def test_add_product(client):
    # Prueba la adición de un nuevo producto con autenticación
    new_product = {'name': 'Aretes', 'price': 15, 'stock': 50}
    headers = {
        'Authorization': 'Basic ' + b64encode(b'admin:secret').decode('utf-8')  # Cabecera de autenticación básica codificada
    }
    rv = client.post('/products', json=new_product, headers=headers)
    assert rv.status_code == 201  # Verifica que el estado de la respuesta sea 201 (Creado)
    assert rv.get_json()['id'] == 4  # Verifica que el ID del nuevo producto sea 4

    # Verifica que el nuevo producto se haya añadido correctamente
    rv = client.get('/products/4')
    assert rv.get_json()['name'] == 'Aretes'  # Verifica que el nombre del producto añadido sea 'Aretes'

def test_add_product_unauthorized(client):
    # Prueba la adición de un nuevo producto sin autenticación
    new_product = {'name': 'Aretes', 'price': 15, 'stock': 50}
    rv = client.post('/products', json=new_product)
    assert rv.status_code == 401  # Verifica que el estado de la respuesta sea 401 (No autorizado)
