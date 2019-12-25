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
        SessionProperties.setSessionProperties(connection, racf, userInfo["name"],
                                               userInfo["email"], userInfo["funcional"])
        return "success"

# Funções de execução SQL

def checkUser(racf, connection):
    searchUserQuery = SQLBuilder.checkUserSQL(racf)
    searchUserResult = pd.read_sql(searchUserQuery, connection)
    if (searchUserResult.empty):
        return False
    else:
        return True

def getUserInfo(racf, connection):
    getUserInfoQuery = SQLBuilder.getUserInfoSQL(racf)
    getUserInfoResult = pd.read_sql(getUserInfoQuery, connection)
    return {"name": getUserInfoResult["usu_nome"].iloc[0],
            "email": getUserInfoResult["usu_email"].iloc[0],
            "funcional": getUserInfoResult["usu_funcional"].iloc[0]}
