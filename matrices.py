
def separar_matrices(columnas, datos, colum_separar):
    matriz_prim = []
    matriz_adj = []
    columnas_prim = int(columnas-colum_separar)
    colum_prim = 0
    colum_adj = 0
    for d in range(0, len(datos)):
        if(colum_prim == columnas_prim):
            if(colum_adj == colum_separar):
                colum_prim = 0
                colum_adj = 0
                colum_prim +=1
                matriz_prim.append(datos[d])
            else:
                colum_adj += 1
                matriz_adj.append(datos[d])
        else:
            colum_prim +=1
            matriz_prim.append(datos[d])

    return [matriz_prim, matriz_adj]

def show_matriz(filas, columnas, datos, adj = False, columnas_adj = None, datos_adj = None):
    for f in range(0, filas):
        print '| ',
        for d in range(f, columnas+f):
            print str(datos[int(d+(columnas-1)*f)]) + "   ",
        if(adj):
            print '|',
            for da in range(f, columnas_adj+f):
                print str(datos_adj[int(da+(columnas_adj-1)*f)]) + "   ",
            print("|")
            print(str("________"*columnas+"________"*columnas_adj))
        else:
            print("|")  
            print(str("______"*columnas))

def det_montante(filas, columnas, datos, pivote_a, msg):
    if(pivote_a == 0):
        return 'Error, pivote = 0'
    if(filas != columnas):
        return 'Error, columnas y filas disparejas'
    if(filas == 2 and columnas == 2):
        if(msg):
            print("")
            print("")
            show_matriz(filas, columnas, datos)
            print("")
            print("")
            print("Pivote anterior: " + str(float(pivote_a)))
            print("")
            print('Determinante: '+ "[("+str(float(datos[0]))+")" + "*(" + str(float(datos[3])) +") - (" + str(float(datos[1])) + ")*(" + str(float(datos[2])) + ")] / (" + str(float(pivote_a)) +")")
            print('Determinante: '+ str(float(((datos[0]*datos[3])-(datos[1]*datos[2]))/pivote_a)))
        else:
            return float(((datos[0]*datos[3])-(datos[1]*datos[2]))/pivote_a)
    else:
        if(msg):
            print("")
            print("")
            show_matriz(filas, columnas, datos)
            print("")
            print("")
            print("Pivote anterior: " + str(float(pivote_a)))
        columna = 1
        fila = 1
        pivote = datos[0]
        nueva_matriz = []
        for f in range(1, filas):
            for d in range(columnas+(1+(columnas*(f-1))), (columnas+(filas-1)+(columnas*(f-1)))+1):
                multp_fila=datos[filas*f]
                multp_colum = datos[columna]
                columna +=1
                dato = float(((datos[d]*pivote) - (multp_colum*multp_fila))/pivote_a)
                nueva_matriz.append(dato)
            columna = 1

        return det_montante(filas-1, columnas-1, nueva_matriz, pivote, msg);

def sistema_ecuaciones_homogeneo(nivel, datos):
    if(float(det_montante(nivel, nivel, datos, 1, False)) != 0):
        print("(*)- Como la determinante no es 0, el sistema solo tiene la solucion trivial")
        det_montante(nivel, nivel, datos, 1, True)
    else:
        print("(*)- Como la determinante es 0, el sistema tiene multiples soluciones")
        det_montante(nivel, nivel, datos, 1, True)
        # Eliminamos la ultima ecuacion
        print("(*)- Eliminamos la ultima ecuacion")
        for delete in range(0, nivel-1):
            datos.pop()
        show_matriz(nivel-1, nivel, datos)
        # Obtenemos la nueva matriz
        columnas = nivel
        filas = nivel-1
        #Cambiamos de signo el ultimo elemento
        print("(*)- Pasamos una variable al otro lado con signo negativo")
        colum_r = 0
        for e in range(0, columnas*filas):
            if(colum_r == (columnas-1)):
                datos[e] *= -1
                colum_r = 0
            else:
                colum_r +=1
        
        sepmat = separar_matrices(nivel, datos, 1)
        show_matriz(nivel-1, nivel-1, sepmat[0], True, 1, sepmat[1])
        #Aplicamos montante con matriz adjunta
        montante_mat_adj(nivel-1,nivel, datos, 1)

def sistema_ecuaciones_heterogeneo(nivel, datos):
    columnas = nivel+1
    filas = nivel
    #Creamos matriz sin constantes
    matriz_det = []
    colum_r = 0
    sepmat = separar_matrices(columnas, datos, 1)
    show_matriz(filas, columnas-1, sepmat[0], True, 1, sepmat[1])
    for e in range(0, columnas*filas):
        if(colum_r == (columnas-1)):
            colum_r = 0
        else:
            matriz_det.append(datos[e])
            colum_r +=1
    if(float(det_montante(nivel, nivel, matriz_det, 1, False)) == 0):
        print("(*)- Como la determinante es 0, el sistema tiene infinitas soluciones")
        det_montante(nivel, nivel, matriz_det, 1, True)
        # Eliminamos la ultima ecuacion
        for delete in range(0, nivel-1):
            datos.pop()
        # Obtenemos la nueva matriz
        filas -= 1
        print("(*)- Eliminamos una de las ecuaciones")
        sepmat = separar_matrices(columnas, datos, 1)
        show_matriz(filas, columnas-1, sepmat[0], True, 1, sepmat[1])
        #Cambiamos de signo al penultimo elemento
        colum_r = 0
        for e in range(0, columnas*filas):
            if(colum_r == (columnas-2)):
                datos[e] *= -1

            if(colum_r == (columnas-1)):
                colum_r = 0
            else:
                colum_r +=1
        print("(*)- Pasamos la ultima variable al otro lado con signo contrario")
        sepmat = separar_matrices(columnas, datos, 2)
        show_matriz(filas, columnas-2, sepmat[0], True, 2, sepmat[1])
        print("")
        #Aplicamos montante con matriz adjunta
        montante_mat_adj(filas,columnas, datos, 2)
    else:
        print("(*)- Como la determinante es diferente de 0, el sistema tiene solucion unica")
        det_montante(nivel, nivel, matriz_det, 1, True)
        print("")
        sepmat = separar_matrices(columnas, datos, 1)
        show_matriz(filas, columnas-1, sepmat[0], True, 1, sepmat[1])
        print("")
        montante_mat_adj(filas,columnas, datos, 1)

def sistema_ecuaciones_redundante(nivel, datos):
    filas = nivel
    columnas = nivel
    #Checamos si es compatible o no con montante
    print("(*)- Obtenemos la determinante para saber si es compatible")
    det = float(det_montante(filas, columnas, datos, 1, False))
    det_montante(filas, columnas, datos, 1, True)
    if(det == 0):
        print("(*)- Como la determinante es 0 el sistema es compatible")
        sepmat = separar_matrices(nivel, datos, 1)
        show_matriz(filas, columnas-1, sepmat[0], True, 1, sepmat[1])
        #Eliminamos la ultima ecuaciones
        print("(*)- Eliminamos una ecuacion")
        for delete in range(0, nivel):
            datos.pop()
        filas -= 1
        sepmat = separar_matrices(nivel, datos, 1)
        show_matriz(filas, columnas-1, sepmat[0], True, 1, sepmat[1])
        montante_mat_adj(filas, columnas, datos, 1)
    else:
        print("(*)- Como la determinante es diferente de 0 el sistema es incompatible por lo que tiene muchas soluciones")
        print("(*)- Resolvemos como sistema heterogeneo eliminando una de sus ecuaciones")
        for delete in range(0, nivel):
            datos.pop()
        show_matriz(filas-1, columnas, datos)
        print("(*)- Ejecutamos el proceso de ecuaciones heterogeneas")
        sistema_ecuaciones_heterogeneo(nivel-1, datos)

def sistema_ecuaciones_defectuoso(filas, columnas, datos):
    #Pasamos una variable al otro lado con signo negativo
    colum_r = 0
    sepmat = separar_matrices(columnas, datos, 1)
    show_matriz(filas, columnas-1, sepmat[0], True, 1, sepmat[1])
    print("(*)- Pasamos una variable al otro lado con signo contrario")
    for e in range(0, columnas*filas):
        if(colum_r == (columnas-2)):
                datos[e] *= -1
        if(colum_r == (columnas-1)):
            colum_r = 0
        else:
            colum_r +=1
    sepmat = separar_matrices(columnas, datos, 2)
    show_matriz(filas, columnas-2, sepmat[0], True, 2, sepmat[1])
    montante_mat_adj(filas, columnas, datos, 2)

def matriz_identidad(nivel, datos):
    colum = 0
    colum_i=0
    fila = 0
    nueva_matriz = []
    d=0
    for i in range(0, 2*nivel*nivel+nivel):
        if(colum == nivel):
            if(colum_i == nivel):
                colum = 0
                colum_i = 0
                fila += 1
            else:
                if(colum_i == fila):
                    colum_i +=1
                    nueva_matriz.append(1)
                else:
                    colum_i += 1
                    nueva_matriz.append(0)
        else:
            nueva_matriz.append(datos[d])
            colum += 1
            d += 1
    return nueva_matriz

def matriz_inversa(nivel, datos):
    show_matriz(nivel, nivel, datos)
    print("")
    print("(*)- Adjuntamos una matriz identidad")
    #Obtenemos la matriz identidad
    matid = matriz_identidad(nivel, datos)
    sepmat = separar_matrices(nivel*2, matid, nivel)
    show_matriz(nivel, nivel, sepmat[0], True, nivel, sepmat[1])
    montante_mat_adj(nivel, 2*nivel, matid, nivel)

def montante_mat_adj(filas, columnas, datos, colum_separar):
    nuevos_datos = []
    pivote_a = 1
    colum = 0
    fila = 0
    print("(*)- Resolvemos con montante")
    #Iteramos en cada una de las filas por los pivotes
    while filas > fila:
        pivote = datos[(fila*columnas)+colum]
        datos_fila = []
        idx_colum = []
        #Guardamos los datos de la fila del pivote
        for dat_idx in range(fila*columnas, columnas+(fila*columnas)):
            datos_fila.append(datos[dat_idx])

        #Guardamos los indices dee las columnas
        for f in range(0, filas):
            idx_colum.append((f*columnas)+colum)
        #Generar nueva matriz
        i_pivote = 0
        num_pivote = 0
        num_fila = 0
        i_colum = 0;
        for i in range(0, filas*columnas):
            if(i >= (fila*columnas) and i < (columnas+(fila*columnas))):
                nuevos_datos.append(datos[i])
            else:
                if(i == i_pivote):
                    nuevos_datos.append(pivote)
                    num_pivote +=1
                    i_pivote = (num_pivote*columnas)+num_pivote
                else:
                    if((i in idx_colum) == False):
                        if(pivote_a == 0):
                            print("(*)- Se encontro que el pivote anterior es 0, por lo que cancelamos el procedimiento:(")
                            return None
                        else:
                            dato = float(((pivote*datos[i])-(datos[i_colum+(columnas*fila)]*datos[(num_fila*columnas)+colum]))/pivote_a)
                            nuevos_datos.append(dato)
                    else:
                        nuevos_datos.append(0)
            if(i_colum == (columnas-1)):
                num_fila +=1
                i_colum = 0
            else:
                i_colum +=1

        datos = nuevos_datos
        print("Pivote anterior: " + str(pivote_a))
        sepmat = separar_matrices(columnas, nuevos_datos, colum_separar)
        show_matriz(filas, columnas-colum_separar, sepmat[0], True, colum_separar, sepmat[1])
        pivote_a = pivote
        fila += 1
        if(filas > fila):
            nuevos_datos = []
        colum += 1
