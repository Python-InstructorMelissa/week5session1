from flask_app.config.mysqlconnection import connectToMySQL

class Animals:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.type = data_dict['type']
        self.sex = data_dict['sex']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.owner = None # placeholder for where the user objects