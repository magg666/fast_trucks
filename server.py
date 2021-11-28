import flask
from flask import Flask, jsonify
# from flask_cors import CORS  # comment for deploy

from app import find_road_between, get_countries, get_countries_between
from validator import is_shortcut_valid

app = Flask(__name__, static_url_path='', static_folder='frontend/build')


# CORS(app)  # comment for deploy


# handling basics errors
@app.errorhandler(405)
def method_not_allowed(error):
    return {'error': "You should not do that..."}


@app.errorhandler(404)
def not_found(error):
    return {'error': 'You should not go there...'}


@app.route('/')
def index():
    return app.send_static_file('index.html')

# page for react requests, methods get and post
@app.route("/serve", methods=['GET', 'POST'])
def serve():
    if flask.request.method == 'GET':

        # get list of all countries to fill form on main page
        countries = get_countries()
        return jsonify(countries)
    else:

        # receives request from react with form values and returns name of countries to travel via
        data = flask.request.json
        start_country = data.get('start')
        end_country = data.get('end')

        if start_country and end_country:

            countries = get_countries_between(end_country, start_country)
            return jsonify(countries)
        else:
            return {'error': 'Choose country'}


# define route to api services. Allowed method - only GET
@app.route('/api/<string:end_country>', methods=["GET"])
def api(end_country):
    if is_shortcut_valid(end_country):
        countries = find_road_between(end_country, start_country="USA")
        return jsonify({'destination': end_country.upper(), 'list': countries})
    else:
        return {'error': "Destination must be three-letter shortcut"}


if __name__ == '__main__':
    app.run()
