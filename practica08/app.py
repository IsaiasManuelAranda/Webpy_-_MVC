import web 

urls= (
    '/', 'application.controllers.clientes.main.Main',
    '/clientes', 'application.controllers.clientes.index.Index',
    '/insert', 'application.controllers.clientes.insert.Insert',
    '/update/(.*)', 'application.controllers.clientes.update.Update',
    '/delete/(.*)', 'application.controllers.clientes.delete.Delete',
    '/view/(.*)', 'application.controllers.clientes.view.View',
    '/productos', 'application.controllers.productos.index.Index_produ',
    '/insert_p', 'application.controllers.productos.insert.Insert_produ',
    '/update_p/(.*)', 'application.controllers.productos.update.Update_produ',
    '/delete_p/(.*)', 'application.controllers.productos.delete.Delete_produ',
    '/view_p/(.*)', 'application.controllers.productos.view.View_produ'
)

if __name__ == '__main__':
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
    