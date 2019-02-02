import web
import config as config

class Delete:
    def __init__(self):
        pass
    
    def GET(self, nombre):
        cliente = config.model_clientes.select_nombre(nombre) #Selecciona el registro que coinicida con el nombre
        return config.render.delete(cliente)

    def POST(self, nombre):
        formulario = web.input()

        nombre = formulario['nombre']
        ape_pat_cli = formulario['ape_pat_cli']
        ape_mat_cli = formulario['ape_mat_cli']
        telefono_cli = formulario['telefono_cli']
        email = formulario['email']

        config.model_clientes.delete_cliente(nombre)
        raise web.seeother('/clientes')
        