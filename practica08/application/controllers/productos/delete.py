import web
import config as config

class Delete_produ:
    def __init__(self):
        pass
    
    def GET(self, codigo):
        producto = config.model_productos.select_producto(codigo) #Selecciona el registro que coinicida con el codigo
        return config.render.delete_p(producto)

    def POST(self, codigo):
        formulario = web.input()

        codigo = formulario['codigo']
        nombre_produ = formulario['nombre_produ']
        existencia = formulario['existencia']
        fecha_caducidad = formulario['fecha_caducidad']
        no_lote = formulario['no_lote']

        config.model_productos.delete_producto(codigo)
        raise web.seeother('/productos')