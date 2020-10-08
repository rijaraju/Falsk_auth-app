from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resource.student import StudentRegister
from resource.details import DetailsRegister

app = Flask(__name__)
app.debug = True
app.config["PROPAGATE_EXCEPTION"] = True
app.secret_key = "****"
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(StudentRegister, "/register")
api.add_resource(DetailsRegister, "/student/<string:name>")
# api.add_resource(DetailsRegister, "/student_details")
if __name__ == "__main__":
    app.run(port=5000, debug=True)
