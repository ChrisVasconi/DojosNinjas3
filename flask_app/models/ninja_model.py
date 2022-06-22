from flask_app.config.mysqlconnections import connectToMySQL
from flask_app import DATABASE


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_one_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) "
        query += "VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_dojo_for_ninja(cls, data):

        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)
        all_ninjas = []
        print(results)
        for row in results:
            all_ninjas.append(row)
        return all_ninjas

    @classmethod
    def show_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s; "
        results = connectToMySQL(DATABASE).query_db(query, data)
