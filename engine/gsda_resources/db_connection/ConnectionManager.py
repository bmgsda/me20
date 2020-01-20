from pyodbc import connect
from engine.gsda_resources.db_connection import DBToken

def create_connection():
    try:
        return connect(DBToken.create_connection_string())
    except:
        pass

def close_connection(connection):
    try:
        connection.close()
        return True
    except:
        pass
