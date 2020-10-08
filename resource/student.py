from flask_restful import Resource, reqparse
from models.student import StudentModel
import mysql.connector


class StudentRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name", type=str, required=True, help="This field cannot be left blank"
    )
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be left blank"
    )

    def post(self):
        data = StudentRegister.parser.parse_args()
        if StudentModel.find_by_name(data["name"]):
            return {"Message": "Student Exits"}
        else:
            # StudentModel.insert_student(data["name"], data["password"])
            return {"Message": "Student does not exists"}

