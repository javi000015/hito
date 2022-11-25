nombre=[]
contrasena=[]
correo = []
tlf=[]

class menu():
    while True:
        print("Elige una opción:\n",
             "1- Inicio de sesion",
             "2- Seleccion de prenda",
             "3 - Compra y pago de los productos"
             "4 - Ver el seguimiento de mi pedido"
            )

        opcion = input("Escribe un número y pulsa enter: ")

        if opcion == "1":
            nombre = input('Nombre de usuario')
            contrasena=input('contraseña de Usario')
            facturacion=input('facturacion del usuario')
            correo = input("Dime tu correo")
            tlf=input('telefono del usuario')
        elif opcion == "2":
            eleccion=int(input("elige un modelo: \n 1 - Ropa de casa , \n 2 - Camisetascasuales , \n 3 - Abrigos , \n 4 - pantaloles de vestir ,\n 5 - Shorts Deportivos ,\n 6 - Gorros , \n 7 - mocasines, \n 8 - bañadores \n"))
            if eleccion==1:
                print('cuesta 10')
            elif eleccion==2:
                print('10')
            elif eleccion==3:
                print('15')
            elif eleccion==4:
                print('15')
            elif eleccion==5:
                print('9')
            elif eleccion==6:
                print('6')
            elif eleccion==7:
                print('19')
            elif eleccion==8:
                print('6')
            else:
                print('elige una prenda correcta')
        elif opcion == "3":
            print(f"La factura ha sido enviada a su correo: {correo}")
        elif opcion == "4":
            print(f"EL PDF con el seguimiento de su pedido ha sido enviado a {tlf} y a su correo {correo}")
menu()