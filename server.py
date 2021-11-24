from flask import Flask, jsonify
from app import find_countries_and_path
from validator import is_shortcut_valid

app = Flask(__name__)


# handling basics errors
@app.errorhandler(405)
def method_not_allowed(error):
    return {'error': "You should not do that..."}


@app.errorhandler(404)
def not_found(error):
    return {'error': 'You should not go there...'}


# define route to api services. Allowed method - only GET
@app.route('/api/<string:end_country>', methods=["GET"])
def api(end_country):
    if is_shortcut_valid(end_country):
        countries, proper_end_country = find_countries_and_path(end_country, start_country="USA")
        return jsonify({'destination': proper_end_country, 'list': countries})
    else:
        return {'error': "Destination must be three-letter shortcut"}


if __name__ == '__main__':
    app.run()
