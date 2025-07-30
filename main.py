from typeguard import value
def calcular_MCD(a, b): #funcion recursiva para calcular el mcd de dos numeros por algoritmo de euclides

    if b==0:
        return a
    else:
        return calcular_MCD(b , a%b)



def cadena_rep(palabra, cantidad): #Funcion para repetir una palabra varias veces
    if cantidad==0:
        return
    else:
        print(palabra)
        return  cadena_rep(palabra, cantidad)


def contar_cadena(palabra, letra): #funcion para contar cuantas veces se repite una letra en una palabra retorna el valor del mcd
    palabra_nueva = palabra.lower()
    letra_nueva = letra.lower()

    if palabra == "":
        return 0
    elif letra_nueva == palabra_nueva[0]:
        return 1 + contar_cadena(palabra[1:], letra)
    else:
        return contar_cadena(palabra[1:], letra)



def convertir_decimalB(numero): #funcion para convertir decimal a binario
    if numero==0:
        return
    else:
        convertir_decimalB(numero%2)


def calc_numeros(n): #funcion recursiva para calcular numeros
    cantidad = len(str(n))
    if cantidad == 1:
        return cantidad
    else:
        return cantidad - calc_numeros(cantidad) +1

fin_menu = True

while fin_menu:
    try:
        print('\t\tBienvenido usuario: ')
        print('1.Calcular MCD\r\n2.Crear cadena repetitiva \r\n3.Contar cuantas veces aparece una letra')
        print('4.Convertir numero decimal a binario \r\n5.Calcular cuantos digitos tiene un numero \r\n6.Salir')
        opcion = int(input('Seleccione una opcion: '))
        match opcion:
            case 1:
                primero = int(input('Ingres el primer numero: '))
                segundo = int(input('Ingrese el segundo numero: '))
                print(f'Valor de MCD: {calcular_MCD(primero, segundo)}')
            case 2: #check
                texto = input('Ingrese la palabra que desea repetir: ')
                cantidad = int(input('Ingrese la cantidad de veces que desea repetir la palabra: '))
                print(f'Numero de repeticiones  {cantidad} : {cadena_rep(texto, cantidad)}')

            case 3: #check
                cadena = input('Ingres el texto: ')
                letra = input('Que letra desea saber cuantas veces se repite: ')
                print(f'Numero de repeticiones letra {letra} : {contar_cadena(cadena, letra)}')

            case 4:
                decimal = input('Ingrese el numero en decial que desea convertir a binario: ')
                convertir_decimalB(decimal)
            case 5: #check
                digitos = int(input('Ingrese el numero del que desea saber cuantos digitos tiene: '))
                print(f'El numero {digitos} tiene: {calc_numeros(digitos)} numeros')
            case 6:
                print('Gracias por usar el sistema')
                fin_menu = False
            case _:
                print('Esta entrada no existe por favor intentelo de nuevo')


    except ValueError:
        print('Ocurrio un error en el ingreso de datos')
