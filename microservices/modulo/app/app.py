from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Modulo(Resource):
    def get(self, num1, num2):
        try:
            result = int(num1) % int(num2)
            return jsonify({"result": result})
        except ZeroDivisionError:
            return jsonify({"error": "division by zero"})


api.add_resource(Modulo, "/<int:num1>/<int:num2>")

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5055,
        host="0.0.0.0"
    )
