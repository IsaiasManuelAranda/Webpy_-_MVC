import web
import config as config

class Insert_produ:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render.insert_p() #Renderiza la pagina insert.html

    def POST(self):
        formulario = web.input() #almacena los datos del formulario
        '''
        Variables que almacenan la obtencion del dato del input de la pagina insert.html
        '''
        codigo = formulario['codigo'] #almacena el nombre escrito en el input
        nombre_produ = formulario['nombre_produ']
        existencia = formulario['existencia']
        fecha_caducidad = formulario['fecha_caducidad']
        no_lote = formulario['no_lote']
        
        config.model_productos.insert_producto(codigo, nombre_produ, existencia, fecha_caducidad, no_lote)
        raise web.seeother('/productos') #al insertar los datos redirecciona al index.html
