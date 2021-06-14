from pymongo import MongoClient

dbuser = 'piotrek'
dbpassword = 'piotrek'
iris_dataset_file_path = './iris.data'

def insert_dataset(iris_dataset_file_path, collection):
    pass


def create_record():
    pass


def retrieve_record():
    pass


def update_record():
    pass


def delete_record():
    pass


def main():
    print('Starting...\n')

    dbHost = input('Provide mongo IP\n')
    dbPort = 27017

    mongo_client = MongoClient(host = str(dbHost) + ':' + str(dbPort), username = dbuser, password = dbpassword)
    print('Created Mongo client\n')

    print("Databases: " + str(mongo_client.list_database_names()), '\n')
    chosen_db_name = input('Choose database to use:\n')
    db = mongo_client[chosen_db_name]

    print('Available collections' + str(db.list_collections()), '\n')
    chosen_collection_name = input('Choose collection to use:\n')
    collection = db[chosen_collection_name]

    insert_dataset(iris_dataset_file_path, collection)

    should_continue = True
    while should_continue:
        operation = input('Choose operation: [(C)reate, (R)etrieve, (U)pdate, (D)elete], exit\n')

        if operation == 'exit':
            should_continue = False
        elif operation == 'C':
            create_record()
        elif operation == 'R':
            retrieve_record()
        elif operation ==  'U':
            update_record()
        elif operation ==  'D':
            delete_record()
        else:
            print("Wrong command\n")


main()

	



