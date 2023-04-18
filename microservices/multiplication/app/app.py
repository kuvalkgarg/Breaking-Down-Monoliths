from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Multiply(Resource):
    def get(self, num1, num2):
        try:
            result = int(num1) * int(num2)
            return jsonify({"result": result})
        except ValueError:
            return jsonify({"error": "invalid input"})


api.add_resource(Multiply, "/<int:num1>/<int:num2>")

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5053,
        host="0.0.0.0"
    )
