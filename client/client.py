from flask import Flask, json
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
    data = requests.get('http://docker-app_serv1_1:8080/info')
    our_dict = data.json()
    our_dict['machine'] = 'client'
    response = app.response_class(
        response=json.dumps(our_dict, sort_keys=False, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
