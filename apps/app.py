"""
These program is a flask based web-application for managing the restaurant orders, having functionalities of managing the
create,update,get,delete orders in database.
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging as log
from logs.logging_logic import log_logic

app = Flask(__name__)
CORS(app)

# Mock database of orders
orders = {
    1: {"category": "Chinese Fast Foods", "status": "Preparing"},
    2: {"category": "Indian Vegetarian", "status": "Preparing"},
    3: {"category": "Tea / Coffee", "status": "Preparing"}
}


@app.route('/')
def home():
    """
    These function is a home route for web application
    :return: str
    """
    log.info("Welcome to Novotel Restaurant!")
    return "Welcome to Novotel Restaurant!"


@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    These function is used to get the order list through order id.
    :param order_id: int
    :return: json
    """
    log.info('get_order function has started...')
    order = orders.get(order_id)  # {"category": "Chinese Fast Foods", "status": "Preparing"}
    try:
        if order:
            log.info(f'For order id={order_id}---->{order}')
            return jsonify(order)  # jsonify({"category": "Chinese Fast Foods", "status": "Preparing"})
        else:
            raise Exception(f'For getting order info, order id ={order_id} has not found')
    except Exception as err:
        log.error(err)
        return jsonify({"error": "Order not found"}), 404
    finally:
        log.info('get_order function has ended...')


@app.route('/order', methods=['POST'])
def create_order():
    """
    These function is used to create an order.
    :return: json
    """
    log.info('create_order function has started...')
    new_order = request.json
    order_id = len(orders) + 1
    orders[order_id] = {"category": new_order["category"], "status": "Preparing"}
    log.debug(f'For order id={order_id}--->{orders[order_id]}')
    log.info(f'"order_id": {order_id}, "status": "Order received"')
    log.info('create_order function has ended...')
    return jsonify({"order_id": order_id, "status": "Order received"}), 201


@app.route('/order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """
    These function is used to update the status of existing order.
    :param order_id: int
    :return: json
    """
    log.info('update_order function has started...')
    try:
        if order_id in orders:
            log.info(f'Updating the orderID={order_id}')
            log.debug(f'Before updating the order = {orders[order_id]}')
            orders[order_id]["status"] = request.json["status"]
            log.debug(f'After Updated the order is = {orders[order_id]}')
            return jsonify({"order_id": order_id, "status": "Order updated"})
        else:
            raise Exception(f'For updating order, Order id = {order_id} has not found')
    except Exception as err:
        log.error(err)
        return jsonify({"error": "Order not found"}), 404
    finally:
        log.info('update_order function has ended...')


@app.route('/order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    These function is used to delete the order through it's order id.
    :param order_id: int
    :return: json
    """
    log.info('delete_order function has started...')
    try:
        if order_id in orders:
            log.info(f'Deleting the order= {orders[order_id]}')
            del orders[order_id]
            log.info(f'Successfully,Deleted the order id = {order_id}')
            return jsonify({"status": "Order deleted"})
        else:
            raise Exception(f'For Deleting Order, Order id= {order_id} has not found')
    except Exception as err:
        log.error(err)
        return jsonify({"error": "Order not found"}), 404
    finally:
        log.info('delete_order function has ended...')


if __name__ == '__main__':
    app.run(debug=True)
