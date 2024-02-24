import csv

with open('datos.csv', 'r') as mis_datos:
    lector = csv.reader(mis_datos)
    next(lector)#omitimos la primera linea que tiene el header
    
    for renglon in lector:
        var_usuario,var_clave,var_mail = renglon
        print(f'usuario: {var_usuario} clave: {var_clave} mail: {var_mail}')
        