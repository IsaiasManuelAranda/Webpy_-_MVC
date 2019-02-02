import config as config

db = config.DB

'''
Metodo para seleccionar todos los registros de la tabla clientes
'''
def select_clientes():
    try:
        return db.select('clientes') #Selecciona todos los registros de la tabla clientes
    except Exception as e:
        print "Model select_clientes Error {}",format(e.args)
        print "Model select_clientes Message {}",format(e.message)
        return None
'''
Metodo para seleccionar el registro cuyo nombre coincida con el de la busqueda
'''
def select_nombre(clientes):
    try:
        return db.select('clientes', where='nombre = $clientes', vars=locals())[0] #Selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}",format(e.args)
        print "Model select_nombre Message {}",format(e.message)
        return None
'''
Metodo para insertar un nuevo registro
'''
def insert_cliente(nombre, ape_pat_cli, ape_mat_cli, telefono_cli, email):
    try:
        return db.insert('clientes', 
        nombre=nombre, 
        ape_pat_cli=ape_pat_cli, 
        ape_mat_cli=ape_mat_cli,
        telefono_cli=telefono_cli,
        email=email) #Inserta un registro en la tabla clientes
    except Exception as e:
        print "Model insert_cliente Error {}",format(e.args)
        print "Model insert_cliente Message {}",format(e.message)
        return None
'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_cliente(nombre):
    try:
        return db.delete('clientes', where='nombre=$nombre', vars=locals())
    except Exception as e:
        print "Model delete_cliente Error {}",format(e.args)
        print "Model delete_cliente Message {}",format(e.message)
        return None
'''
Metodo para actualizar el registro por el nombre dado
'''
def update_cliente(nombre, ape_pat_cli, ape_mat_cli, telefono_cli, email):
    try:
        return db.update('clientes',
            ape_pat_cli=ape_pat_cli,
            ape_mat_cli=ape_mat_cli,
            telefono_cli=telefono_cli,
            email=email,
            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_cliente Error {}",format(e.args)
        print "Model update_cliente Message {}",format(e.message)
        return None
