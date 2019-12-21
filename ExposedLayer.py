import eel
from engine.controller import Login
from engine.controller import SessionProperties

# Funções de exposição (API-like)

@eel.expose
def tryLogin(racf, password):
    return Login.c_tryLogin(racf, password)

# Setter e triggers para execução do programa

eel.init("web")
eel.start("login.html")
