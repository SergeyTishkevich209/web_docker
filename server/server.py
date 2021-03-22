from flask import Flask, request, json, jsonify
from random import randint
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/', methods=['GET'])
def index():
    our_dict = {
        'string': 'try another address, for example /info'
    }
    return jsonify(our_dict)


@app.route('/info', methods=['GET'])
def info():
    our_dict = {
        'string': 'Success',
        'user agent': str(request.user_agent),
        'time': str(datetime.utcnow()),
        'host': request.base_url,
        'charset': request.charset,
        'random id': randint(1000000, 9000000),
        'machine': 'server'
    }
    response = app.response_class(
        response=json.dumps(our_dict, sort_keys=False, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/<string:some_str>', methods=['GET'])
def redirection_to(some_str):
    our_dict = {
        'string': 'incorrect address !!!!!',
        'user agent': str(request.user_agent),
        'time': str(datetime.utcnow()),
        'host': request.host,
        'some in address': some_str,
    }
    response = app.response_class(
        response=json.dumps(our_dict, sort_keys=False, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
