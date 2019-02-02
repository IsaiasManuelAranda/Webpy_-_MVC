import web
import config as config

class Index_produ:
    def __init__(self):
        pass
    
    def GET(self):
        productos = config.model_productos.select_productos().list() #Selecciona los registros de productos y los lista
        return config.render.index_p(productos) #Envia los datos como parametro para la pagina web
