import json

from app.create_app import db, app
from flask import request

from app.models import User, Order, Offer


@app.route("/users", methods=['GET', 'POST'])
def work_users():
    if request.method == 'GET':
        result = []
        for user in db.session.query(User).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result),
            mimetype="application/json",
            status=200
        )

    if request.method == 'POST':
        data = request.json

        db.session.add(
            User(
                **data
            )
        )

        return app.response_class(
            json.dumps("Ok"),
            mimetype="application/json",
            status=200
        )


@app.route("/users/<int:bid>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def work_user(bid):
    if request.method == 'GET':
        result = []
        for user in db.session.query(User).filter(User.id == bid).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result),
            mimetype="application/json",
            status=200
        )

    if request.method == 'POST':
        data = request.json

        db.session.add(
            User(
                **data
            )
        )

    if request.method == 'PUT':
        data = request.json
        db.session.query(User).get(bid)
        db.id = data.get("id")
        db.session.commit()

    if request.method == 'DELETE':
        db.session.query(User).filter(User.id == bid).delete()
        db.session.commit()

        return app.response_class(
            json.dumps("Ok"),
            mimetype="application/json",
            status=200
        )


@app.route("/orders", methods=['GET', 'POST'])
def work_orders():
    if request.method == 'GET':
        result = []
        for user in db.session.query(Order).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result),
            mimetype="application/json",
            status=200
        )

    if request.method == 'POST':
        data = request.json

        db.session.add(
            Order(
                **data
            )
        )

        return app.response_class(
            json.dumps("Ok"),
            mimetype="application/json",
            status=200
        )


@app.route("/orders/<int:bid>", methods=['GET', 'POST', 'DELETE'])
def work_order(bid):
    if request.method == 'GET':
        result = []
        for user in db.session.query(Order).filter(Order.id == bid).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result, ensure_ascii=False),
            mimetype="application/json",
            status=200
        )

    if request.method == 'POST':
        data = request.json

        db.session.add(
            Order(
                **data
            )
        )

    if request.method == 'DELETE':
        db.session.query(Order).filter(Order.id == bid).delete()
        db.session.commit()

        return app.response_class(
            json.dumps("Ok"),
            mimetype="application/json",
            status=200
        )


@app.route("/offers", methods=['GET', 'POST'])
def work_offers():
    if request.method == 'GET':
        result = []
        for user in db.session.query(Offer).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result),
            mimetype="application/json",
            status=200
        )

    if request.method == 'POST':
        data = request.json

        db.session.add(
            Offer(
                **data
            )
        )

        return app.response_class(
            json.dumps("Ok"),
            mimetype="application/json",
            status=200
        )


@app.route("/offers/<int:bid>", methods=['GET', 'PUT', 'DELETE'])
def work_offer(bid):
    if request.method == 'GET':
        result = []
        for user in db.session.query(Offer).filter(Offer.id == bid).all():
            result.append(
                user.return_data()
            )
        return app.response_class(
            json.dumps(result, ensure_ascii=False),
            mimetype="application/json",
            status=200
        )

    if request.method == 'PUT':
        data = request.json
        offer = db.session.query(Offer).get(bid)
        offer.id = data.get("id")

        db.session.commit()

    if request.method == 'DELETE':
        db.session.query(Offer).filter(Offer.id == bid).delete()
        db.session.commit()

        return app.response_class(
            json.dumps("Ok"),
            mimetype="application/json",
            status=200
        )


if __name__ == '__main__':
    app.run(debug=True)
