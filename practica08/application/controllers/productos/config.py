import web 
import application.models.model_productos as model_productos #importa el modelo productos

render = web.template.render('application/views/productos/', base='master_p') #Configura la ubicacion del archivo
