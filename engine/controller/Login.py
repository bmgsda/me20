from engine.controller import Session
from engine.database import SQLExecutor
from engine.gsda_resources.db_connection import ConnectionManager
from engine.gsda_resources.common import Util

# Funções chamadas pela camada de exposição
def try_login():
    windows_user_info = Util.get_windows_user_info()
    racf = windows_user_info['racf']
    connection = ConnectionManager.create_connection()
    if (connection is None):
        return "Falha de conexão ao Banco de Dados"
    else:
        user_info = check_user(racf, connection)
        if not (user_info):
            return "Usuário "+racf+" não cadastrado"
        else:
            Session.set_session_connection(connection)
            Session.set_session_user_data(user_info["id"], racf,
                                          user_info["name"],
                                          user_info["email"],
                                          user_info["funcional"])
            return "success"

# Funções Auxiliares
def check_user(racf, connection):
    search_user_result = SQLExecutor.search_user(racf, connection)
    if (search_user_result.empty):
        return False
    else:
        return {"id": search_user_result["usu_id"].iloc[0],
                "racf": search_user_result["usu_racf"].iloc[0],
                "name": search_user_result["usu_nome"].iloc[0],
                "email": search_user_result["usu_email"].iloc[0],
                "funcional": search_user_result["usu_funcional"].iloc[0]}
