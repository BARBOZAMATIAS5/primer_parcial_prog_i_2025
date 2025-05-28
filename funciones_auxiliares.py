### aca se encuentran los validadores, casteos, validaciones de ingreso y limitador
### de ingreso, es decir ingresar un numero de min x a max y

def validar_numero(n: str) -> bool:
    '''
    Verifica si lo ingresado son numeros enteros
    Parametros: n -> str
    Return: boolean
    '''
    if n.isdigit():
        return True

    return False
    
def castear_numero(n: str) -> int:
    '''
    Castea lo pasado por parametro a entero si es posible |
    Paramentros: n -> str |
    Retorna: int (en lo posible, de lo contrario un mensaje
                por consola para reintentar el ingreso)
    '''
    if validar_numero(n):
        return int(n)
        
    else:
        print("Error al ingresar el numero, intentelo nuevamente")
    
def ingresar_numero(mensaje: str) -> int | float:
    '''
    Pide al usuario ingresar un int, en caso que no sea, va a
    solicitarlo nuevamente |
    Parametros: mensaje -> str |
    Return: int
    '''
    while True:
        numero = castear_numero(input(mensaje))
        if type(numero) == int or type(numero) == float:
            return numero

def limitador_de_ingreso(mensaje: str, min: int, max: int) -> int:
    '''
    Limita el ingreso del usuario, dependiendo de los parametros pasados |
    Parametros: mensaje -> str, min -> int, max -> int |
    Retorn: int
    '''
    while True:
        numero_ingresado = ingresar_numero(mensaje)
        if min <= numero_ingresado <= max:
            return numero_ingresado
        else:
            print(f"Error, ingresar nuevamente un numero entre {str(min)} y {str(max)}")