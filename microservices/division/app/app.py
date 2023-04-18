from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class Div(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('num1', type=int, required=True)
        self.parser.add_argument('num2', type=int, required=True)
        super(Div, self).__init__()

    def get(self):
        args = self.parser.parse_args()
        return {'result': args['num1'] / args['num2']}


api.add_resource(Div, '/')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5054,
        host='0.0.0.0'
    )
