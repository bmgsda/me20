import eel
from engine.controller import Login
from engine.controller import SessionProperties

# Funções de exposição (API-like)

@eel.expose
def tryLogin(racf, password):
    return Login.c_tryLogin(racf, password)
