import mysql.connector
import json


class DetailsModel:
    def __init__(self, _id, name, password, address, phone, score):
        self.Name = name
        self.password = password
        self.id = _id
        self.Address = address
        self.Phone = phone
        self.Score = score

    @classmethod
    def get_details(cls, name):
        connection = mysql.connector.connect(
            user="root", password="password", host="localhost", database="api"
        )
        cursor = connection.cursor()
        query = "select id, Name, Address, Phone, Score from data where Name = %s"
        cursor.execute(query, (name,))
        row = cursor.fetchone()
        connection.close()
        return row

    @classmethod
    def update_details(cls, _id, password, Address, Phone, Score, Name):
        connection = mysql.connector.connect(
            user="root", password="password", host="localhost", database="api"
        )
        cursor = connection.cursor()
        query = "update data set id=%s, password=%s, Address=%s, Phone=%s, Score=%s where Name = %s"
        val = (_id, password, Address, Phone, Score, Name)
        cursor.execute(query, val)
        connection.commit()
        connection.close()

    @classmethod
    def insert_details(cls, _id, Name, Address, password, Phone, Score):
        # print(details)
        connection = mysql.connector.connect(
            user="root", password="password", host="localhost", database="api"
        )
        cursor = connection.cursor()
        query = "INSERT INTO data (id, Name, password,Address, Phone,Score) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (_id, Name, password, Address, Phone, Score)
        cursor.execute(query, val)
        connection.commit()
        connection.close()

    @classmethod
    def delete_details(cls, name):
        connection = mysql.connector.connect(
            user="root", password="password", host="localhost", database="api"
        )
        cursor = connection.cursor()
        query = "delete from data where Name = %s"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()


# update data set Address='Address',Phone='Phonr', Score=10 where Name = 'Rija Raju'
