import eel
from engine.gsda_resources.common import Util
from engine.controller import Login
from engine.controller import Session

# Funções de exposição (API-like)

@eel.expose
def requestLogin(racf):
    return Login.try_login(racf)

@eel.expose
def requestSessionUserInfo():
    return Session.get_session_user_info()

@eel.expose
def requestWindowsUserInfo():
    return Util.get_windows_user_info()

@eel.expose
def requestForcedExit():
    return Util.force_exit()
