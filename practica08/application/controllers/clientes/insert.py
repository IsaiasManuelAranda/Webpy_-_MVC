import web
import config as config

class Insert:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render.insert() #Renderiza la pagina insert.html

    def POST(self):
        formulario = web.input() #almacena los datos del formulario
        '''
        Variables que almacenan la obtencion del dato del input de la pagina insert.html
        '''
        nombre = formulario['nombre'] #almacena el nombre escrito en el input
        ape_pat_cli = formulario['ape_pat_cli']
        ape_mat_cli = formulario['ape_mat_cli']
        telefono_cli = formulario['telefono_cli']
        email = formulario['email']
        
        config.model_clientes.insert_cliente(nombre,ape_pat_cli,ape_mat_cli,telefono_cli,email)
        raise web.seeother('/clientes') #al insertar los datos redirecciona al index.html
