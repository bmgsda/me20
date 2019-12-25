def checkUserSQL(racf):
    return "SELECT USU_RACF FROM USU_USUARIO WHERE USU_RACF = UPPER('" + racf + "')"

def getUserInfoSQL(racf):
    return "SELECT USU_NOME, USU_EMAIL, USU_FUNCIONAL FROM USU_USUARIO WHERE USU_RACF = UPPER('" + racf + "')"
