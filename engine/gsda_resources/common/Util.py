import os
import pwd
from sys import exit
import pandas
from engine.gsda_resources.db_connection import ConnectionManager
from engine.gsda_resources.versioning import AppData

def get_windows_user_info():
    windows_user = pwd.getpwuid(os.getuid())
    return {'racf': windows_user[0].upper(),
            'name': windows_user[4].replace(',','')}

def get_app_data():
    return AppData.app_data

def get_app_config():
    return AppData.app_config

def get_current_version():
    app_data = get_app_data()
    return app_data['version']

def get_latest_version():
    connection = ConnectionManager.create_connection()
    get_latest_version_query = "SELECT VER_NUM FROM VER_VERSAO ORDER BY VER_ID DESC LIMIT 1"
    get_latest_version_result = pandas.read_sql(get_latest_version_query, connection)
    ConnectionManager.close_connection(connection)
    return get_latest_version_result["ver_num"].iloc[0]

def force_exit():
    exit()
