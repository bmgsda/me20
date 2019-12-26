# Variáveis globais da sessão (valerão para todo a sessão do programa)

connection = None
userRacf = None
userName = None
userEmail = None
userFuncional = None

# Funções chamadas pela camada de exposição

def c_getSessionUserInfo():
    treatedUserNameList = userName.title().split()[:2]
    treatedUserName = treatedUserNameList[0] + " " + treatedUserNameList[1]
    return {"userRacf": userRacf,
            "userName": treatedUserName,
            "userEmail": userEmail,
            "userFuncional": userFuncional}


# Funções chamadas pela camada de controle

def setSessionProperties(conn, racf, name, email, funcional):
    global connection
    global userRacf
    global userName
    global userEmail
    global userFuncional
    connection = conn
    userRacf = racf
    userName = name
    userEmail = email
    userFuncional = funcional
