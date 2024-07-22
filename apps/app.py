"""
These program is a flask based web-application for managing the restaurant ORDERS,
having functionalities of managing the create,update,get,delete ORDERS in database.
"""
# Importing 3rd party packages
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Importing local packages
import constants as const
from constants import *
from logs.logging_logic import *

# Creating application Instances
app = Flask(__name__, template_folder='html_scripts')
CORS(app)


@app.route('/')
def home():
    """
    These function is a home route for web application
    :return: str
    """
    log.info("Welcome to Novotel Restaurant!")
    return render_template('index.html')


@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    These function is used to get the order list through order id.
    :param order_id: int
    :return: json
    """
    log.info(f'{const.NAME} - get_order function has started...')
    order = ORDERS.get(order_id)  # {"category": "Chinese Fast Foods", "status": "Preparing"}
    try:
        if order:
            log.debug(f'{const.NAME} - For order id={order_id}---->{order}')
            return jsonify(order)
        raise Exception(f'For getting order info, order id ={order_id} has not found')
    except Exception as err:
        log.error(err)
        return jsonify(error=f"Order id={order_id} not found", status=const.FAILED), 404
    finally:
        log.info(f'{const.NAME} - get_order function has ended...')


@app.route('/order', methods=['POST'])
def create_order():
    """
    These function is used to create an order.
    :return: json
    """
    log.info(f'{const.NAME} - create_order function has started...')
    try:
        new_order = request.json
        order_id = len(ORDERS) + 1
        ORDERS[order_id] = {"category": new_order["category"], "status": "Preparing"}
        log.debug(f'{const.NAME} - For order id={order_id}--->{ORDERS[order_id]}')
        log.debug(f'{const.NAME} - "order_id": {order_id}, "status": "Order received"')
        return jsonify({"order_id": order_id, "status": "Order received"}), 200
    finally:
        log.info(f'{const.NAME} - create_order function has ended...')


@app.route('/order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """
    These function is used to update the status of existing order.
    :param order_id: int
    :return: json
    """
    log.info(f'{const.NAME} - update_order function has started...')
    try:
        if order_id in ORDERS:
            log.debug(f'{const.NAME} - Updating the orderID={order_id}')
            log.debug(f'{const.NAME} - Before updating the order = {ORDERS[order_id]}')
            ORDERS[order_id]["status"] = request.json["status"]
            log.debug(f'{const.NAME} - After Updated the order is = {ORDERS[order_id]}')
            return jsonify({"order_id": order_id, "status": "Order updated"}), 200
        raise Exception(f'{const.NAME} - For updating order, Order id = {order_id} has not found')
    except Exception as err:
        log.error(err)
        return jsonify(error=f"Order id={order_id} not found", status=const.FAILED), 400
    finally:
        log.info(f'{const.NAME} - update_order function has ended...')


@app.route('/order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    These function is used to delete the order through it's order id.
    :param order_id: int
    :return: json
    """
    log.info(f'{const.NAME} - delete_order function has started...')
    try:
        if order_id in ORDERS:
            log.debug(f'{const.NAME} - Deleting the order= {ORDERS[order_id]}')
            del ORDERS[order_id]
            log.debug(f'{const.NAME} - Successfully,Deleted the order id = {order_id}')
            return jsonify({"status": "Order deleted"}), 200
        raise Exception(f'{const.NAME} - For Deleting Order, Order id= {order_id} has not found')
    except Exception as err:
        log.error(err)
        return jsonify({"error": "Order not found"}), 404
    finally:
        log.info(f'{const.NAME} - delete_order function has ended...')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
