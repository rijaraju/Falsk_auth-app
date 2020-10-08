from werkzeug.security import safe_str_cmp
from models.student import StudentModel


def authenticate(name, password):
    student = StudentModel.find_by_name(name)
    if student and safe_str_cmp(student.password, password):
        return student


def identity(payload):
    identity = payload["identity"]
    return StudentModel.find_by_id(identity)

