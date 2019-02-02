import config as config

db = config.DB

'''
Metodo para seleccionar todos los registros de la tabla productos
'''
def select_productos():
    try:
        return db.select('productos') #Selecciona todos los registros de la tabla productos
    except Exception as e:
        print "Model select_productos Error {}",format(e.args)
        print "Model select_productos Message {}",format(e.message)
        return None
'''
Metodo para seleccionar el registro cuyo nombre coincida con el de la busqueda
'''
def select_producto(codigo):
    try:
        return db.select('productos', where='codigo = $codigo', vars=locals())[0] #Selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_codigo Error {}",format(e.args)
        print "Model select_codigo Message {}",format(e.message)
        return None
'''
Metodo para insertar un nuevo registro
'''
def insert_producto(codigo, nombre_produ, existencia, fecha_caducidad, no_lote):
    try:
        return db.insert('productos', 
        codigo=codigo,
        nombre_produ=nombre_produ,
        existencia=existencia,
        fecha_caducidad=fecha_caducidad,
        no_lote=no_lote
        ) #Inserta un registro en la tabla productos
    except Exception as e:
        print "Model insert_producto Error {}",format(e.args)
        print "Model insert_producto Message {}",format(e.message)
        return None
'''
Metodo para eliminar un registro que coincida con el codigo recibido
'''
def delete_producto(codigo):
    try:
        return db.delete('productos', where='codigo=$codigo', vars=locals())
    except Exception as e:
        print "Model delete_producto Error {}",format(e.args)
        print "Model delete_producto Message {}",format(e.message)
        return None
'''
Metodo para actualizar el registro por el codigo dado
'''
def update_producto(codigo, nombre_produ, existencia, fecha_caducidad, no_lote):
    try:
        return db.update('productos',
            codigo=codigo,
            nombre_produ=nombre_produ,
            existencia=existencia,
            fecha_caducidad=fecha_caducidad,
            no_lote=no_lote,
            where='codigo=$codigo',
            vars=locals())
    except Exception as e:
        print "Model update_producto Error {}",format(e.args)
        print "Model update_producto Message {}",format(e.message)
        return None
