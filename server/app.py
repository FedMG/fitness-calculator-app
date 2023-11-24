from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


# from flask import Flask
# from flask_restful import Api, Resource
# # from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# api = Api(app)

# class HelloWorld(Resource):
#     def get(self, name, test):
#         return { "name": name, "test": test  }

#     def post(self):
#         return { "data": "Posted" }


# api.add_resource(HelloWorld, "/helloWorld/<string:name>/<int:test>")

# if __name__ == "__main__":
#     # only for development "debug = True"
#     app.run(debug=True)






