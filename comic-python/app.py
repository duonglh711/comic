from flask import Flask, render_template, make_response
from flask_restful import Api
from http import HTTPStatus


app = Flask(__name__)
api = Api(app)


@app.route('/heath-check/')
@app.route('/')
def heath_check():
    return make_response({
        'Message': 'OK',
        'Status Code': HTTPStatus.OK
    }, HTTPStatus.OK)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
