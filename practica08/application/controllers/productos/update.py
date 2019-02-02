import web
import config as config

class Update_produ:
    def __init__(self):
        pass

    def GET(self, codigo):
        producto = config.model_productos.select_producto(codigo) #Selecciona el registro que coinicida con el nombre
        return config.render.update_p(producto) #Envia el registro y renderiza update.html

    def POST(self, nombre_produ):
        formulario = web.input()

        codigo = formulario['codigo'] #almacena el nombre escrito en el input
        nombre_produ = formulario['nombre_produ']
        existencia = formulario['existencia']
        fecha_caducidad = formulario['fecha_caducidad']
        no_lote = formulario['no_lote']

        config.model_productos.update_producto(codigo, nombre_produ, existencia, fecha_caducidad, no_lote)
        raise web.seeother('/productos')
        