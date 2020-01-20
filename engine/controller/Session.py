# Variáveis globais da sessão

session_connection = {
    'connection': None
}

session_user_data = {
    'user_id': None,
    'user_racf': None,
    'user_name': None,
    'user_email': None,
    'user_funcional': None
}

# Funções chamadas pela camada de exposição

def get_session_user_data():
    #treated_user_name_list = session_data['user_name'].title().split()[:2]
    #treated_user_name = treated_user_name_list[0] + " " + treated_user_name_list[1]
    return session_user_data


# Funções chamadas pela camada de controle

def set_session_user_data(id, racf, name, email, funcional):
    global session_user_data
    session_user_data = {
        'user_id': id,
        'user_racf': racf,
        'user_name': name,
        'user_email': email,
        'user_funcional': funcional
    }

def set_session_connection(connection):
    global session_connection
    session_connection = {
        'connection': connection
    }
