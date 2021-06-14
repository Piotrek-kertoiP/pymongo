from pymongo import MongoClient

dbuser = 'piotrek'
dbpassword = 'piotrek'
iris_dataset_file_path = './iris.data'

def insert_dataset(iris_dataset_file_path, collection):
    pass


def main():
    print('Starting...\n')
    
   # mongo_client = MongoClient(host = 'localhost:27017', username = dbuser, password = dbpassword)
    mongo_client = MongoClient(host = '172.18.0.3:27017', username = dbuser, password = dbpassword)
    print('Created Mongo client\n')

    print("Databases: ", mongo_client.list_database_names(), '\n')
    chosen_db_name = input('Choose database to use:\n')
    db = mongo_client[chosen_db_name]

    print('Available collections', db.list_collections(), '\n')
    chosen_collection_name = input('Choose collection to use:\n')
    collection = db[chosen_collection_name]

    insert_dataset(iris_dataset_file_path, collection)

    should_continue = True
    while should_continue:
        operation = input('Choose operation: [(C)reate, (R)etrieve, (U)pdate, (D)elete], exit\n')

        if operation == 'exit':
            should_continue = False

main()

	



