import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import setup_db , Coffeeshops, Visited
from flask_cors import CORS
from auth import requires_auth




app = Flask(__name__)
setup_db(app)





@app.route('/visited', methods=['GET'])
@requires_auth('get:visited')
def visited(jwt):
    visitedar = Visited.query.all()
    formatted_visited = [visited.format() for visited in visitedar]
    print(formatted_visited)
    return jsonify({'visited': formatted_visited})


@app.route('/visited', methods=['POST'])
@requires_auth('post:visited')
def add_visited(jwt):
    try:
        Visited(name=request.get_json()['name'],
             recommended=request.get_json()['recommended']).insert()
        return jsonify({'done': 'yes'}), 201
    except Exception:
        return jsonify({'done': 'no'}), 500

@app.route('/coffeeshops', methods=['GET'])
# @requires_auth('get:name')
def all(jwt):
    coffeeshop = Coffeeshops.query.all()
    formatted_coffeeshops = [coffeeshops.format() for coffeeshops in coffeeshop]
    print(formatted_coffeeshops)
    return jsonify({'coffeeshop': formatted_coffeeshops})


@app.route('/coffeeshops', methods=['POST'])
@requires_auth('post:name')
def add_coffeeshops(jwt):
    try:
        Coffeeshops(name=request.get_json()['name'],
             rate=request.get_json()['rate'],
             recommended=request.get_json()['recommended']).insert()
        return jsonify({'done': 'yes'}), 201
    except Exception:
        return jsonify({'done': 'no'}), 500


@app.route('/coffeeshops/<id>', methods=['PATCH'])
@requires_auth('patch:name')
def edit_togp(jwt, id):
    try:
        coffeeshops = Coffeeshops.query.get(id)
        if not coffeeshops:
            return abort(404)
        if 'name' in request.get_json():
            coffeeshops.name = request.get_json()['name']

        if 'rate' in request.get_json():
            coffeeshops.rate = request.get_json()['rate']

        if 'recommended' in request.get_json():
            coffeeshops.recommended = request.get_json()['recommended']

        coffeeshops.update()
        print(coffeeshops)
        return jsonify({'done': 'yes'}), 200
    except Exception:
        return jsonify({'done': 'no'}), 500


@app.route('/coffeeshops/<id>', methods=['DELETE'])
@requires_auth('delete:name')
def delete_coffeeshops(jwt, id):
    try:
        coffeeshops = coffeeshops = Coffeeshops.query.get(id)
        if not coffeeshops:
            return jsonify({'done': 'no'}), 404
        coffeeshops.delete()
        return jsonify({'done': 'yes'}), 200
    except Exception:
        return jsonify({'done': 'no'}), 500




    @app.errorhandler(401)
    def not_found_error(error):
        return jsonify({'error': 'unauthorized access'}), 401


    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'api not found'}), 404

    @app.errorhandler(422)
    def server_error(error):
        return jsonify({'error': 'you reach Unprocessable api'}), 422



    @app.errorhandler(500)
    def server_error(error):
        return jsonify({'error': 'server error'}), 500