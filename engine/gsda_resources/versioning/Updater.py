from pymsgbox import alert
from shutil import rmtree
from pathlib import Path
from distutils.dir_util import copy_tree
from engine.gsda_resources.common import Util

def verify_version():
    current_version = Util.get_current_version()
    latest_version = Util.get_latest_version()
    if (current_version == latest_version):
        return True
    else:
        update_version()
        Util.force_exit()

def update_version():
    app_data = Util.get_app_data()
    source_path = app_data['source-path']
    destiny_path = str(Path().absolute())
    destiny_old_path = destiny_path + '/old/'
    try:
        rmtree(destiny_old_path)
    except:
        pass
    copy_tree(destiny_path, destiny_old_path)
    copy_tree(source_path, destiny_path)
    alert('O aplicativo foi atualizado para sua última versão.\nPor favor, abra-o novamente.', 'Atualização de Versão')
