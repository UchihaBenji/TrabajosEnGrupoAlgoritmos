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
    elif opc=='2':
        print('Precio de cada zapato: 25$')
        while True:
            try:
                c=int(input('Introduzca cuantos zapatos desea comprar: '))
                break
            except ValueError:
                print('No es un valor numerico. Intentalo de nuevo')
                time.sleep(2)
                os.system("cls")
        precio=c*25.00
        if c<10:
            print('No hay descuento, el precio es de: ', "{:.2f}".format(precio))
        elif c>=10 and c<20:
            descuento=precio*0.1
            total=precio-descuento
            print ('Precio bruto: ', "{:.2f}".format(precio), ' Descuento: ', "{:.2f}".format(descuento),' Precio total: ', "{:.2f}".format(total))
        elif c>=20 and c<40:
            descuento=precio*0.2
            total=precio-descuento
            print ('Precio bruto: ', "{:.2f}".format(precio), ' Descuento: ', "{:.2f}".format(descuento),' Precio total: ', "{:.2f}".format(total))
        elif c>=40:
            descuento=precio*0.4
            total=precio-descuento
            print ('Precio bruto: ', "{:.2f}".format(precio), ' Descuento: ', "{:.2f}".format(descuento),' Precio total: ', "{:.2f}".format(total))
    elif opc=='3':
        while True:
            try:
                x=float(input('Introduzca su compra: '))
                break
            except ValueError:
                print('No es un valor numerico. Intentalo de nuevo')
                time.sleep(2)
                os.system("cls")
        while (m!='A' and m!='a' and m!='B' and m!='b' and m!='C' and m!='c'):
                m=input('Introduzca su tipo de membresia (A, B, C): ')
                if (m!='A' and m!='a' and m!='B' and m!='b' and m!='C' and m!='c'):
                    print('Opcion invalida')
        if x<100:
            print('Total a pagar: ', "{:.2f}".format(x), '. No hay descuentos')
        elif x>=100 and x<250:
            if m=='A' or m=='a':
                pagar=x - (x*0.1)
            else:
                pagar=x
            print('Membresia: ', m,' Total a pagar: ', "{:.2f}".format(pagar))
        elif x>=250 and x<350:
            if m=='A' or m=='a':
                pagar=x - (x*0.1)
            elif m=='B' or m=='b':
                pagar=x - (x*0.15)
            else:
                pagar=x 
            print('Membresia: ', m,' Total a pagar: ', "{:.2f}".format(pagar))
        elif x>=350:
            if m=='A' or m=='a':
                pagar=x - (x*0.1)
            elif m=='B' or m=='b':
                pagar=x - (x*0.15)
            elif m=='C' or m=='c':
                pagar=x - (x*0.2)
            print('Membresia: ', m,' Total a pagar: ', "{:.2f}".format(pagar))
        m='u'
    elif opc=='4':
        print('Gracias por utilizar el programa')
        salida=True
    else:
        print('Introduzca una opcion valida')
        time.sleep(2)
        os.system("cls")