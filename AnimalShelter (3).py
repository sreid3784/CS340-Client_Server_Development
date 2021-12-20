from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username=None, password=None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:    
            self.client = MongoClient('mongodb://%s:%s@localhost:53694/AAC' %(username,password))
        else:
            self.client = MongoClient('mongodb://localhost:5364')
            
        self.database = self.client['AAC']
        
# Complete this create method to implement the C in CRUD.

    

    def create(self, data):
        if data is not None:
            #Insert the data, and return true if successful.
            self.database.animals.insert(data)  # data should be dictionary    
            return True
        else:
            #data was invalid.
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD. 
    def read(self, data):
        if data is not None:
            #return all records that match.
            return self.database.animals.find(data)
            print("read complete!")
        else:
            #Data was invalid.
            raise Exception("Nothing to search, because data parameter is empty")
            return False
        
 #update method to implemement the U in CRUD
    def update(self,lookupInfo,newInfo):
        if lookupInfo is not None:
            tempRecord = self.read(lookupInfo)
            return self.database.animals.update(lookupInfo,newInfo)
        else:
            raise Exception("Record parameter is empty")
            return False
        
 #delete method to implement the D in CRUD

    def delete(self,record):
        if record is not None:
            return self.database.animals.remove(record) #record is a dictionary
        else:
            raise Exception("Record parameter is empty")
            return False

