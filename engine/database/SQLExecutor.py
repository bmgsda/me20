import pandas
from engine.database import SQLBuilder

def search_user(racf, connection):
    search_user_query = SQLBuilder.search_user_SQL(racf)
    search_user_result = pandas.read_sql(search_user_query, connection)
    return search_user_result
