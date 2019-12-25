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
        userInfo = getUserInfo(racf,connection)
        SessionProperties.connection = connection
        SessionProperties.userRacf = racf
        SessionProperties.userName = userInfo["name"]
        SessionProperties.userEmail = userInfo["email"]
        SessionProperties.userFuncional = userInfo["funcional"]
        return "success"

# Funções auxiliares

def checkUser(racf, connection):
    searchUserQuery = SQLBuilder.checkUserSQL(racf)
    searchUserResult = pd.read_sql(searchUserQuery, connection)
    if (searchUserResult.empty):
        return False
    else:
        return True

def getUserInfo(racf, connection):
    searchUserQuery = SQLBuilder.getUserInfoSQL(racf)
    searchUserResult = pd.read_sql(searchUserQuery, connection)
    return {"name": searchUserResult["usu_nome"].iloc[0],
            "email": searchUserResult["usu_email"].iloc[0],
            "funcional": searchUserResult["usu_funcional"].iloc[0]}
