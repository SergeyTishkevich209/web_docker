from flask import Flask, json
from random import randint
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/', methods=['GET'])
def index():
    our_dict = {
        'number': randint(1000000, 9999999999)
    }
    response = app.response_class(
        response=json.dumps(our_dict, sort_keys=False, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(port=5001, debug=True)
