from funciones_auxiliares import *
### 1
def cargar_matriz_notas() -> list:
    '''
    Se ingresa la cantidad de alumnos y se ingresa la cantidad de notas,
    despues solicita ingresar las notas.
    Parametro: ninguno
    Return: list
    '''
    matriz_notas = []
    ingreso_alumnos = ingresar_numero("Ingrese la cantidad de alumnos: ")
    notas_alumnos = ingresar_numero("Ingrese la cantidad de notas: ")

    for n in range(ingreso_alumnos):
        lista_aux = []
        for m in range(notas_alumnos):
            notas = limitador_de_ingreso(
                f"Ingrese la nota del alumno {n+1}: ", 1, 10)
            lista_aux.append(notas)
        matriz_notas.append(lista_aux)
    
    return matriz_notas

### la carga de matriz primero crea una lista vacia y despues pide los datos de cantidad de alumnos y notas,
### siendo n --> alumnos, m --> notas. Despues de ingresar, se creara el primer for que tendra la funcionalidad
### de iterar los alumnos y se crea una lista auxiliar para almacenar dentro de ella, las notas que se tendran que
### ingresar en el siguiente for anidado. Al terminar la carga de notas, se hace un append a la lista fuera de los
### bucles, permitiendo la conformacion de los alumnos (filas(n)) y las notas (columnas(m))

### 2
def porcentaje_aprobados(matriz_alumnos: list) -> None:
    '''
    Se calcula el porcentaje de examenes aprobados de cada alumno
    Parametros: matriz_alumnos: list
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

alumnos = cargar_matriz_notas()
print(alumnos)
porcentaje_aprobados(alumnos)

