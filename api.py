# Tahap lanjut hubungkna ke sisi frontend dengan menggunakan Flask menggunakan React.js

from flask import Flask, jsonify, request
from flask_cors import CORS
from customer_zaki import CustomerZaki
from product_zaki import ProductZaki
from order_zaki import OrderZaki

app = Flask(__name__)
CORS(app)  # Mengizinkan akses dari frontend (React)

# Endpoint untuk mendapatkan semua customer
@app.route('/api/customers', methods=['GET'])
def get_customers():
    customer = CustomerZaki()
    customer.cursor.execute("SELECT * FROM customers_zaki")
    rows = customer.cursor.fetchall()
    result = [{"id": row[0], "name": row[1]} for row in rows]
    return jsonify(result)

# Endpoint untuk menambahkan customer
@app.route('/api/customers', methods=['POST'])
def add_customer():
    data = request.json
    cus_id = data['id']
    cus_name = data['name']
    customer = CustomerZaki()
    customer.add_zaki(cus_id, cus_name)
    return jsonify({"message": "Customer added successfully"}), 201

# Endpoint untuk mendapatkan semua produk
@app.route('/api/products', methods=['GET'])
def get_products():
    product = ProductZaki()
    product.cursor.execute("SELECT * FROM product_zaki")
    rows = product.cursor.fetchall()
    result = [{"id": row[0], "name": row[1], "price": row[2]} for row in rows]
    return jsonify(result)

# Endpoint untuk mendapatkan semua order
@app.route('/api/orders', methods=['GET'])
def get_orders():
    order = OrderZaki()
    order.cursor.execute("SELECT * FROM orders_zaki")
    rows = order.cursor.fetchall()
    result = [{"id": row[0], "customer_id": row[1], "product_name": row[2], "order_date": row[3]} for row in rows]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
