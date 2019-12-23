import eel
from screeninfo import get_monitors
from engine import ExposedLayer

# Tamanho da janela e adequação ao centro da tela

width = get_monitors()[0].width
height = get_monitors()[0].height
sizeWidth = width*0.7
sizeHeight = height*0.75
posWidth = (width-sizeWidth)/2
posHeight = (height-sizeHeight)/2

# Inicialização

eel.init("web")
eel.start("views/login.html", size=(sizeWidth, sizeHeight), position=(posWidth,posHeight))
