import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db
from app.models import Offer, Order, User


def load_data(path):
    with open(path) as file:
        return json.load(file)


def load_offer(path):
    offers = load_data(path)

    for offer in offers:

        db.session.add(
            Offer(
                **offer
            )
        )

        db.session.commit()


def load_order(path):
    orders = load_data(path)

    for order in orders:

        db.session.add(
            Order(
                **order
            )
        )

        db.session.commit()


def load_user(path):
    users = load_data(path)

    for user in users:

        db.session.add(
            User(
                **user
            )
        )

        db.session.commit()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}
    app.config['SQLALCHEMY_ECHO'] = True

    with app.app_context():
        db.init_app(app)
        db.create_all()
        offer = load_offer('../data/offers.json')
        user = load_user('../data/users.json')
        orders = load_order('../data/orders.json')

    return app


app = create_app()
