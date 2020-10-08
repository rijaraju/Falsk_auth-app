from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.details import DetailsModel
from models.student import StudentModel
import mysql.connector


class DetailsRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "id", type=str, required=True, help="This field cannot be left blank"
    )
    parser.add_argument(
        "Name", type=str, required=True, help="This field cannot be left blank"
    )
    parser.add_argument(
        "Address", type=str, required=True, help="This field cannot be left blank"
    )
    parser.add_argument(
        "Password", type=str, required=False, help="This field cannot be left blank"
    )
    parser.add_argument(
        "Phone", type=str, required=True, help="This field cannot be left blank"
    )
    parser.add_argument(
        "Score", type=int, required=True, help="This field cannot be left blank"
    )

    @jwt_required()
    def get(self, name):
        # print(name)
        details = DetailsModel.get_details(name)
        if details:
            return details
        else:
            return {"Message": "Student not found"}

    def post(self, name):
        if StudentModel.find_by_name(name):
            return {"Message": "Student exists"}
        data = DetailsRegister.parser.parse_args()
        # print(data)
        DetailsModel.insert_details(
            data["id"],
            data["Name"],
            data["Address"],
            data["Password"],
            data["Phone"],
            data["Score"],
        )
        return {"Msg": "Student inserted"}

    @jwt_required()
    def delete(self, name):
        if StudentModel.find_by_name(name) is None:
            return {"Message": "Student does not exists"}
        else:
            DetailsModel.delete_details(name)
            return {"Message": "Student deleted"}

    # @jwt_required
    def put(self, name):
        if StudentModel.find_by_name(name) is None:
            return {"Message": "Student does not exists"}
        data = DetailsRegister.parser.parse_args()
        DetailsModel.update_details(
            data["id"],
            data["Password"],
            data["Address"],
            data["Phone"],
            data["Score"],
            data["Name"],
        )
        return {"Msg": "Student details updated"}

