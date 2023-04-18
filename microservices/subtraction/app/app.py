from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Subtraction(Resource):
    def get(self, num1, num2):
        result = int(num1) - int(num2)
        return jsonify({"result": result})


api.add_resource(Subtraction, "/<int:num1>/<int:num2>")

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5052,
        host="0.0.0.0"
    )
