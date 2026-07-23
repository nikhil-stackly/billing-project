from flask import Blueprint, jsonify

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify({
        "message": "Welcome to Billing Project API",
        "status": "Running"
    })


@main.route("/health")
def health():
    return jsonify({
        "status": "OK"
    })


@main.route("/customers")
def customers():
    return jsonify({
        "message": "Customer API"
    })


@main.route("/products")
def products():
    return jsonify({
        "message": "Product API"
    })


@main.route("/invoices")
def invoices():
    return jsonify({
        "message": "Invoice API"
    })


@main.route("/payments")
def payments():
    return jsonify({
        "message": "Payment API"
    })
