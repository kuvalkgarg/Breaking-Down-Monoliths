from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Add(Resource):
    def get(self, num1, num2):
        return {'result': int(num1) + int(num2)}


api.add_resource(Add, '/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5051,
        host='0.0.0.0'
    )
