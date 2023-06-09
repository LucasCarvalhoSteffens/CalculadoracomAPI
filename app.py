from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)



class Multiply(Resource):
    def get(self):
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        result = num1 * num2
        return jsonify({'result': result})

class Divide(Resource):
    def get(self):
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        result = num1 / num2
        return jsonify({'result': result})

class Add(Resource):
    def get(self):
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        result = num1 + num2
        return jsonify({'result': result})

class Subtract(Resource):
    def get(self):
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        result = num1 - num2
        return jsonify({'result': result})


api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')
api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')

if __name__ == '__main__':
    app.run()
