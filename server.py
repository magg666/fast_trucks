from flask import Flask, jsonify, send_from_directory
from flask_restful import Api, Resource, reqparse
# from flask_cors import CORS
from api.api import HelloApiHandler

from app import find_countries_and_path
from validator import is_shortcut_valid

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
# CORS(app)
api2 = Api(app)

# handling basics errors
@app.errorhandler(405)
def method_not_allowed(error):
    return {'error': "You should not do that..."}


@app.errorhandler(404)
def not_found(error):
    return {'error': 'You should not go there...'}

# @app.route("/", defaults={'path':''})
# def serve(path):
#     return send_from_directory(app.static_folder, 'index.html')

# define route to api services. Allowed method - only GET
@app.route('/api/<string:end_country>', methods=["GET"])
def api(end_country):
    if is_shortcut_valid(end_country):
        countries, proper_end_country = find_countries_and_path(end_country, start_country="USA")
        return jsonify({'destination': proper_end_country, 'list': countries})
    else:
        return {'error': "Destination must be three-letter shortcut"}

#
# api2.add_resource(HelloApiHandler, '/flask/hello')

if __name__ == '__main__':
    app.run()
