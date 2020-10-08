import mysql.connector


class StudentModel:
    def __init__(self, _id, name, password):
        self.id = _id
        self.name = name
        self.password = password

    @classmethod
    def find_by_name(cls, name):
        connection = mysql.connector.connect(
            user="root", password="password", host="localhost", database="api"
        )
        cursor = connection.cursor()
        query = "select id, Name,password from data where Name =%s"
        # print(name)
        cursor.execute(query, (name,))
        row = cursor.fetchone()
        if row:
            student = cls(*row)
        else:
            student = None
        connection.close()
        return student

    @classmethod
    def find_by_id(cls, _id):
        connection = mysql.connector.connect(
            user="root", password="password", host="localhost", database="api"
        )
        cursor = connection.cursor()
        query = "select id, Name,password from data where id = %s"
        cursor.execute(query, (_id,))
        row = cursor.fetchone()
        if row:
            student = cls(*row)
        else:
            student = None
        connection.close()
        return student

