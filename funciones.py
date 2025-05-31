from funciones_auxiliares import *
### 1
def cargar_matriz_notas() -> list:
    '''
    Se ingresa la cantidad de alumnos y se ingresa la cantidad de notas,
    despues solicita ingresar las notas |
    Parametro: ninguno |
    Return: list
    '''
    matriz_notas = []
    ingreso_alumnos = ingresar_numero("Ingrese la cantidad de alumnos: ")
    notas_alumnos = ingresar_numero("Ingrese la cantidad de notas: ")

    if ingreso_alumnos > 0 and notas_alumnos > 0:
        for n in range(ingreso_alumnos):
            lista_aux = []
            for m in range(notas_alumnos):
                notas = limitador_de_ingreso(
                    f"Ingrese la nota del alumno {n+1}: ", 1, 10)
                lista_aux.append(notas)
            matriz_notas.append(lista_aux)
    else:
        print("Error al ingresar los alumnos y las notas, deben ser mayores a 0")
    
    return matriz_notas

### la carga de matriz primero crea una lista vacia y despues pide los datos de cantidad de alumnos y notas,
### siendo n --> alumnos, m --> notas. Despues de ingresar, se creara el primer for que tendra la funcionalidad
### de iterar los alumnos y se crea una lista auxiliar para almacenar dentro de ella, las notas que se tendran que
### ingresar en el siguiente for anidado. Al terminar la carga de notas, se hace un append a la lista fuera de los
### bucles, permitiendo la conformacion de los alumnos (filas(n)) y las notas (columnas(m)). Retorna una matriz

### 2
def porcentaje_aprobados(matriz_alumnos: list) -> None:
    '''
    Se calcula el porcentaje de examenes aprobados de cada alumno |
    Parametros: matriz_alumnos: list |
    Return: None
    '''
    cantidad_notas = len(matriz_alumnos[0])
    for i in range(len(matriz_alumnos)):
        contador_aprobadas = 0
        suma_notas = 0

        for j in range(len(matriz_alumnos[i])):
            if matriz_alumnos[i][j] > 5:
                contador_aprobadas += 1
            suma_notas += matriz_alumnos[i][j]
        
        porcentaje = contador_aprobadas / cantidad_notas * 100
        promedio = suma_notas / cantidad_notas

        print(
            f"El alumno {i+1} aprobó {contador_aprobadas}, con un porcentaje de {porcentaje}%")
        print(
            f"y su promedio es de: {promedio}")

### la funcionalidad calcular el porcentaje de examenes aprobados de cada alumno, donde dentro del primer for
### creo (de crear) las variables de contador_aprobadas, encargada de contar los examenes aprobados y suma_notas
### que será un acumulador que sumará cada nota del alumno. Ambas operaciones se irán llevando a cabo en el for anidado
### donde compruebo con un if las notas que sean mayores a 5, se las considerará aprobadas, sumando +1 al contador y fuera
### del if, siendo innecesario tener que cumplir esta condicion, se irán sumando las anotas. Dentro del primer for, posterior
### a lo anterior, se calcularán los porcentajes y promedios, imprimiendo por consola los parciales que aprobó cada alumno, 
### su porcentaje al igual que su promedio. No retornará nada.

### alumnos = cargar_matriz_notas()
### print(alumnos)
### porcentaje_aprobados(alumnos)

### 3
def mejor_promedio(matriz_alumnos: list) -> list:
    '''
    Se encarga de calcular los promedios de los alumnos y devolverá
    el alumno el indice del alumno con mejor promedio y su promedio
    mas alto |
    Parametros: matriz_alumnos -> list |
    Return: list -> [indice, promedio]
    '''
    promedio_alumnos = []
    cantidad_notas = len(matriz_alumnos[0])
    for i in range(len(matriz_alumnos)):
        suma_notas = 0

        for j in range(len(matriz_alumnos[i])):
            suma_notas += matriz_alumnos[i][j]
        
        promedio = suma_notas / cantidad_notas
        promedio_alumnos.append([promedio])
    
    return maximo(promedio_alumnos)

### esta funcion lo que va hacer es, a la matriz pasada por parametro, va a crear una lista auxiliar y contabilizar
### la cantidad de notas. Dntro del primer for se crea la variable que se encargará de guardar la suma de las notas del alumno
### que se encuentre en la iteracion, esta suma se lleva a cabo en el for anidado de "j", terminando esta suma
### se realizará el calculo del promedio y el appendeo del mismo a la lista auxiliar creada al principio. Claramente
### la variable auxiliar encargada de guardar las sumas de las notas del alumno, se reiniciará a 0 en cada iteracion de cada alumno
### de "i". Al final se usará la funcion maximo(), creada en funciones_auxiliares que devolverá el indice y el promedio

### print(mejor_promedio(alumnos))
### 4
def buscar_nota(matriz_alumnos: list, nota_buscada: int) -> list:
    '''
    Busca dentro de la matriz la nota pasada por parametro |
    Parametros: matriz_alumons -> list, nota_buscada -> int |
    Return: list -> [[indice, columna]]
    '''
    filas_columas = []
    for i in range(len(matriz_alumnos)):
        for j in range(len(matriz_alumnos[i])):
            if matriz_alumnos[i][j] == nota_buscada:
                filas_columas.append([i, j])

    return filas_columas

### se encarga de buscar la nota mediante el parametro nota_buscada, dentro de la matriz pasada tambien por parametro. Al principio
### se crea una lista auxiliar donde se almacenarán todas las posiciones donde la nota_buscada se encuentren en la matriz.
### Usando dos for anidades, encargados del recorrido de toda la matriz, donde en el segundo for se hará cargo de la comparacion
### de si la posicion actual tiene el mismo valor que la nota_buscada. En los casos que pase, se realizará un appendeo a la lista 
### creada al principio y en caso de que no, se devolverá la lista vacía.

### menu opciones ###
def imprimir_menu() -> None:
    '''
    Imprime el menu de las opciones
    Parametros: None
    Return: None
    '''
    print("---Menu opciones---")
    print("1. Cargar alumnos y notas")
    print("2. Mostrar porcentajes de aprobacion de los alumnos y sus promedios")
    print("3. Mostrar indice del alumno con mejor promedio y su promedio")
    print("4. Ingresar nota buscada")
    print("0. Cerrar sistema")


def alumnos_menu_principal():
    '''
    Encargado del funcionamiento del sistema
    Parametros: None
    Return: None
    '''
    imprimir_menu()
    print("---------------------------------")
    return limitador_de_ingreso("Ingrese una de las opciones: ", 0, 4)

def alumnos_app():

    matriz_alumnos = []

    while True:
        opcion = alumnos_menu_principal()

        match opcion:
            case 1:
                print("---------------------------------")
                matriz_alumnos = cargar_matriz_notas()
                print("---------------------------------")
            case 2:
                print("---------------------------------")
                if len(matriz_alumnos) > 0:
                    porcentaje_aprobados(matriz_alumnos)
                else:
                    print("Error, la matriz se encuentra vacía")
                print("---------------------------------")
            case 3:
                print("---------------------------------")
                if len(matriz_alumnos) > 0:
                    print(mejor_promedio(matriz_alumnos))
                else:
                    print("Error, la matriz se encuentra vacía")
                print("---------------------------------")
            case 4:
                print("---------------------------------")
                if len(matriz_alumnos) > 0:
                    notas = buscar_nota(matriz_alumnos, limitador_de_ingreso(
                           "Ingrese la nota que quiere buscar: ", 1, 10))
                    if len(notas) == 0:
                        print("No se encontraron notas con ese numero")
                    else:
                        print(notas)
                else:
                    print("Error, la matriz se encuentra vacía")
                print("---------------------------------")
            case 0:
                break