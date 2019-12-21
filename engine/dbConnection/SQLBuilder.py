def checkUserSQL(racf):
    return "SELECT USU_RACF FROM USU_USUARIO WHERE USU_RACF = UPPER('" + racf + "')"
