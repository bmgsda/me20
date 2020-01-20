def search_user_SQL(racf):
    return "SELECT * FROM USU_USUARIO WHERE USU_RACF = UPPER('" + racf + "')"
