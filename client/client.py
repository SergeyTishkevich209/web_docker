from flask import Flask, json
from datetime import datetime
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/', methods=['GET'])
def index():
    try:
        data = requests.get('http://web-docker_superserver_1:8080').json()
    except requests.exceptions.ConnectionError as e:
        data = {}
    our_dict = {
        'string': 'this is json',
        'time': str(datetime.utcnow()),
        'random id': data.get('number'),
        'machine': 'server'
    }
    response = app.response_class(
        response=json.dumps(our_dict, sort_keys=False, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)
