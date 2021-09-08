import os
import time
salida=False
m=' '
while not salida:
    print ('1) Presentacion')
    print ('2) Tienda de zapatos')
    print ('3) Supermercado')
    print ('4) Despedida')
    while True:
        try:
            opc=input('Elija una opcion: ')
            break
        except ValueError:
            print('No es un valor numerico. Intentalo de nuevo')
            time.sleep(2)
            os.system("cls")
    if opc=='1':
        print('UNIVERSIDAD TECNOLÓGICA DE PANAMÁ')
        print('FACULTAD DE INGENIERÍAD DE SISTEMAS COMPUTACIONALES')
        print('DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS')
        print('LABORATORIO 2')
        print('FC-FISC-1-8-2016')
        print('Integrantes :')
        print ('Benjamin Rodriguez')
        print('Samuel Nuñez')
        print('Susana Gonzalez')
        print('Humberto Carcamo')
        print('Angel diaz')
        time.sleep(2)
        os.system("cls")
    else:
        print('Introduzca una opcion valida')
        time.sleep(2)
        os.system("cls")