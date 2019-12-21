import pyodbc

def createConnection(racf, password):
    connectionString = createConnectionString(racf, password)
    try:
        connection = pyodbc.connect(connectionString)
        return connection
    except:
        pass

def createConnectionString(racf, password):
    connectionString = (
        "DRIVER={PostgreSQL Unicode};"
        "DATABASE=DB000;"
        "UID="+racf+";"
        "PWD="+password+";"
        "SERVER=localhost;"
        "PORT=5432;"
    )
    return connectionString
