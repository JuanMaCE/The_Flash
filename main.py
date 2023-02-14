print('Nombre: Juan Marcos Cortés Enriquez')
print('Facultad: Ingenieria')
print('Carrera: Ingenieria en Informatica y Sistemas ')
print('Semestre: 1')
print('No Carnet: 1530623')

import os

mi_ubicacion = os.getcwd()
if os.path.exists("modulos"):
    print("La carpeta ya existe")
else:
    os.mkdir(mi_ubicacion + "\\modulos")
    archivo = open('./modulos/prueba.txt', 'w')
    archivo.write('Hola mundo')
    archivo.close()
