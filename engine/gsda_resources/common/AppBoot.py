import eel
from screeninfo import get_monitors
from engine.gsda_resources.versioning import Updater
from engine.gsda_resources.common import Util
from engine import ExposedLayer

def boot():
    # Mecanismo de verificação e atualização da versão
    Updater.verify_version()

    # Recupera as configurações de tamanho da janela
    app_config = Util.get_app_config()
    width_multiplier = app_config['width-multiplier']
    height_multiplier = app_config['height-multiplier']

    # Recupera as informações de resolução do monitor
    width = get_monitors()[0].width
    height = get_monitors()[0].height

    # Define o tamanho e posição da janela
    size_width = width*width_multiplier
    size_height = height*height_multiplier
    pos_width = (width-size_width)/2
    pos_height = (height-size_height)/2

    # Inicialização
    eel.init("interface")
    eel.start("views/login.html", size=(size_width, size_height), position=(pos_width,pos_height))
