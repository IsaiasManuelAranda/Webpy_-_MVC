import web
import config as config

class Index:
    def __init__(self):
        pass
    
    def GET(self):
        clientes = config.model_clientes.select_clientes().list() #Selecciona los registros de personas y los lista
        return config.render.index(clientes) #Envia los datos como parametro para la pagina web
 