from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class GCD(Resource):
    def get(self):
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        return {'result': self.compute_gcd(num1, num2)}

    @staticmethod
    def compute_gcd(num1, num2):
        if num2 == 0:
            return num1
        else:
            return GCD.compute_gcd(num2, num1 % num2)


api.add_resource(GCD, '/')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5057,
        host='0.0.0.0'
    )
