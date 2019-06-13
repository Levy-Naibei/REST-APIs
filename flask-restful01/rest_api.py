from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from views import Orders

api.add_resource(Orders, '/','/<id>')


if __name__ == '__main__':
	app.run(debug = True)
