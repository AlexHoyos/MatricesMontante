from colors import red, green, blue, bold
from matrices import det_montante,sistema_ecuaciones_homogeneo,sistema_ecuaciones_heterogeneo, sistema_ecuaciones_redundante, sistema_ecuaciones_defectuoso, matriz_inversa
def show_menu():
    print blue("<-=--------------------------------------------=->")
    print blue("<-= Hola! Bienvenido al resolvedor de matrices =->")
    print blue("<-=        Desarrollado por Alex Hoyos         =->")
    print blue("<-=    Debe seleccionar una opcion del menu    =->")
    print blue("<-=--------------------------------------------=->")
    print blue("> 1. Obtencion de determinante de matriz")
    print blue("> 2. Resolver sistema de ecuaciones")
    print blue("> 3. Obtener la matriz inversa")
    print red("> 0. Salir")

option = -1
while(option != 0):
    
    show_menu()
    option = int(input("Has elegido: "))
    if(option == 1):
        nivel = int(input("De cuantas filas y columnas es la matriz: "))
        datos_total = int(nivel * nivel)
        datos = []
        print("Ingrese los datos: ")
        for d in range(0, datos_total):
            dato = float(input())
            datos.append(dato)
        proce = bool(input("Desea obtener el procedimiento? 1=Si 0=No "))
        print det_montante(nivel,nivel,datos,1,proce)
        exit_o = bool(input("Desea realizar mas calculos? 1=Si 0=No "))
        if(exit_o):
            option = -1
        else:
            option = 0
    if(option == 2):
        print blue(">>> Selecciona una de las siguientes opciones")
        print blue("> 1. Sistema de ecuaciones homogeneo")
        print blue("> 2. Sistema de ecuaciones redundante")
        print blue("> 3. Sistema de ecuaciones defectuoso")
        print blue("> 0. Salir")
        sub_opt = int(input("Has elegido: "))
        if(sub_opt == 1):
            nivel = int(input("Cuantas variables y ecuaciones son: "))
            cero = bool(input("Sus ecuaciones son igual a 0: 1=Si 0=No"))
            if(cero):
                datos_total = int(nivel*nivel)
            else:
                datos_total = int(nivel*(nivel+1))
            datos = []
            print("Ingrese los datos (no incluya variables): ")
            for d in range(0, datos_total):
                dato = float(input())
                datos.append(dato)
            if(cero):
                sistema_ecuaciones_homogeneo(nivel, datos)
            else:
                sistema_ecuaciones_heterogeneo(nivel, datos)
        if(sub_opt == 2):
            variables = int(input("Numero de variables: "))
            nivel = variables+1
            datos = []
            print("Ingrese los datos: ")
            for d in range(0, nivel*nivel):
                dato = float(input())
                datos.append(dato)
            sistema_ecuaciones_redundante(nivel,datos)
        if(sub_opt == 3):
            columnas = float(input("Ingrese el numero de variables: "))
            filas = columnas-1
            columnas +=1
            datos = []
            print("Ingrese los datos: ")
            for d in range(0, filas*columnas):
                dato = float(input())
                datos.append(dato)
            sistema_ecuaciones_defectuoso(filas, columnas, datos)
        else:
            option = -1
    if(option == 3):
        nivel = int(input("De que nivel es la matriz (2:2x2, 3:3x3, 4:4x4 N:NxN): "))
        datos = []
        print("Ingrese los datos: ")
        for d in range(0, int(nivel*nivel)):
            dato = float(input())
            datos.append(dato)
        matriz_inversa(nivel, datos)
    else:
        print blue("(*)-> HASTA LUEGO! <-(*)")
        option = 0
