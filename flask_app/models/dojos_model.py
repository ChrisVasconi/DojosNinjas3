from unittest import result
from flask_app.config.mysqlconnections import connectToMySQL
from flask_app import DATABASE
from flask_app.models.ninja_model import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_new_dojo(cls, data):
        query = "INSERT INTO dojos (name) "
        query += "VALUES (%(name)s );"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def show_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []

        for row in results:
            all_dojos.append(cls(row))

        return all_dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id= %(id)s; "
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        if len(results) > 0:
            return cls(results[0])
        return False

    @classmethod
    def get_ninjas_from_dojos(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('ninjas').query_db(query, data)
        dojo = cls(result[0])
        for row_from_db in results:

            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["ninjas.first_name"],
                "last_name": row_from_db["ninjas.last_name"],
                "age": row_from_db["ninjas_age"]
            }
            dojo.ninjas.append(Ninja.Ninja(ninja_data))
            return dojo
