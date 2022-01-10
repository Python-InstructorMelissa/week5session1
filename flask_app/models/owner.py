from flask_app.config.mysqlconnection import connectToMySQL

class Owner:
    db_name = "animal_vet"
    # constructor
    def __init__(self, data_dict): #pass in a whole dictionary
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
    # instance methods - affect a particular instance (object)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def email_length(self):
        return len(self.email)
    # class methods -affect any instance
    # static methods 
    # class methods go below here

    @classmethod
    def get_all_owners(cls):
        # GOAL- Take a list of dict and return a list of objects

        # things to do:
        # create a query to send to the database
        query = "SELECT * FROM owners;"
        # send it the db
        results_from_db = connectToMySQL(cls.db_name).query_db(query) # list of dict

        # parse the results from the database and turn them into objects
        all_owners = [] 
        # print(results_from_db)
        for row in results_from_db: 
            this_owner = cls(row)
            all_owners.append(this_owner)
        

        return all_owners # list of objects
    # make a class method for creating a new owner in the datbase using MYSQL.