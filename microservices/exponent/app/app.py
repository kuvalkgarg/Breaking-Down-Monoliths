from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Exp(Resource):
    def get(self):
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        return {'result': num1 ** num2}


api.add_resource(Exp, '/')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5056,
        host='0.0.0.0'
    )
