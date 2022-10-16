from main.configuration.mongo_db_connection import MongoDBClient


if __name__=='__main__':
    mongodb_client=MongoDBClient()
    print(mongodb_client.client.list_database_names())
    print("collection name:",mongodb_client.database.list_collection_names())