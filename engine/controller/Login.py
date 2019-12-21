import pandas as pd
from engine.dbConnection import CreateConnection
from engine.dbConnection import SQLBuilder
from engine.controller import SessionProperties

# Funções chamadas pela camada de exposição

def c_tryLogin(racf, password):
    connection = CreateConnection.createConnection(racf, password)
    if (connection is None):
        return "Falha de conexão ao SQL"
    elif not (checkUser(racf, connection)):
        return "Usuário não cadastrado"
    else:
        SessionProperties.connection = connection
        SessionProperties.racf = racf
        return "success"

# Funções auxiliares

def checkUser(racf, connection):
    searchUserQuery = SQLBuilder.checkUserSQL(racf)
    searchUserResult = pd.read_sql(searchUserQuery, connection)
    if (searchUserResult.empty):
        return False
    else:
        return True
