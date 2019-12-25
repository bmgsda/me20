import eel
from engine.controller import Login
from engine.controller import SessionProperties

# Funções de exposição (API-like)

@eel.expose
def tryLogin(racf, password):
    return Login.c_tryLogin(racf, password)

@eel.expose
def getSessionUserInfo():
    userRacf = SessionProperties.userRacf
    userEmail = SessionProperties.userEmail
    userFuncional = SessionProperties.userFuncional
    userName = SessionProperties.userName
    treatedUserNameList = userName.title().split()[:2]
    treatedUserName = treatedUserNameList[0] + " " + treatedUserNameList[1]
    return {"userRacf": userRacf,
            "userName": treatedUserName,
            "userEmail": userEmail,
            "userFuncional": userFuncional}
