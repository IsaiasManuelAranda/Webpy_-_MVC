import web 
import application.models.model_clientes as model_clientes #importa el modelo clientes

render = web.template.render('application/views/clientes/', base='master') #Configura la ubicacion del archivo