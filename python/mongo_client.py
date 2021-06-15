from pymongo import MongoClient
import iris_dataset

dbuser = 'piotrek'
dbpassword = 'piotrek'


def create_record(collection):
    sepalLength = float(input("Type in sepalLength\n"))
    sepalWidth = float(input("Type in sepalWidth\n"))
    petalLength = float(input("Type in petalLength\n"))
    petalWidth = float(input("Type in petalWidth\n"))
    species = input("Type in species\n")

    dictionary = {
        "sepalLength": sepalLength,
        "sepalWidth": sepalWidth,
        "petalLength": petalLength,
        "petalWidth": petalWidth,
        "species": species
    }

    result = collection.insert_one(dictionary)
    print('Inserted document, id = ', result.inserted_id)


def retrieve_records(collection):
    results = collection.find()
    for x in results:
        print(x)


def delete_record(collection):
    print("Specify filters to delete only records you want to delete. "
          "If you want to delete all, type in 'none' two times\n")

    key = input("Give key name on which you want to filter\n")
    value = input("Give value associated with given key on which you want to filter\n")
    if key != 'species' and key != 'none':
        value = float(value)

    if key == 'none' and value == 'none':
        query = {}
    else:
        query = {key: value}

    results = collection.delete_many(query)
    print(results.deleted_count, " documents deleted.")


def insert_iris(collection):
    collection.insert_many(iris_dataset.dataset)
    print('Inserted dictionary')


def main():
    print('Starting...\n')

    dbHost = input("Provide mongo IP, for example: 172.18.0.3. If you don't know it, use command:\n "
                   "docker inspect mongo_mongo_1 | grep IPAddress\n")
    dbPort = 27017

    mongo_client = MongoClient(host=str(dbHost) + ':' + str(dbPort), username=dbuser, password=dbpassword)
    print('Created Mongo client\n')

    print("Databases: " + str(mongo_client.list_database_names()), '\n')
    chosen_db_name = input('Choose database to use. If you want to use another database, type its name. '
                           'It will be created:\n')
    db = mongo_client[chosen_db_name]

    print('Available collections', db.list_collections(), '\n')
    chosen_collection_name = input('Choose collection to use. If you want to use another collection, type its name. '
                                   'It will be created:\n')
    collection = db[chosen_collection_name]

    should_continue = True
    while should_continue:
        operation = input('Choose operation: (C) create, (R) retrieve,(D) delete, (I) insert iris, (exit) exit\n')

        if operation == 'exit':
            should_continue = False
        elif operation == 'C':
            create_record(collection)
        elif operation == 'R':
            retrieve_records(collection)
        elif operation == 'D':
            delete_record(collection)
        elif operation == 'I':
            insert_iris(collection)
        else:
            print("Wrong command\n")


main()
