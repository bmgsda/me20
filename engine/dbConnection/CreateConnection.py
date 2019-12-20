import pyodbc

def createConnectionString(racf, password):
    connectionString = (
        "DRIVER={PostgreSQL Unicode};"
        "DATABASE=DB000;"
        "UID="+racf+";"
        "PWD="+password+";"
        "SERVER=localhost;"
        "PORT=5432;"
    )
    print("Connection String created.")
    print(connectionString)
    return connectionString

def createConnection(racf, password):
    connectionString = createConnectionString(racf, password)
    try:
        connection = pyodbc.connect(connectionString)
        print("Connection created.")
        resultSearchUser = connection.execute("SELECT USU_RACF FROM USU_USUARIO WHERE USU_RACF = '" + racf + "'")
        print("Query executed.")
        if (resultSearchUser is None):
            return "Sem cadastro na base"
        else:
            return connection
    except:
        return "Falha de conexão ao SQL"
