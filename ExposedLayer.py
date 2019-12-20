import eel
from engine.dbConnection import CreateConnection

# Variáveis de sessão
sessionConnection = None
userRacf = None

# Funções de exposição (API-like)

@eel.expose
def tryLogin(racf, password):
    print("TryLogin triggered.")
    connectionResponse = CreateConnection.createConnection(racf, password)
    print("Response given.")
    if (isinstance(connectionResponse, str)):
        print("Failed login.")
        return connectionResponse
    else:
        sessionConnection = connectionResponse
        userRacf = racf
        print("Success login.")
        print(racf)
        return "success"

# Setter e triggers para execução do programa

eel.init("web")
eel.start("login.html")
