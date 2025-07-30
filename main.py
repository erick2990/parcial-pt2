from typeguard import value

fin_menu = True

def calc_numeros(n):
    cantidad = len(str(n)) #hace la conversion de datos para saber cuantos datos hay
    if n==0:
        return 0
    else:
        return cantidad[1:]



while fin_menu:
    try:
        print('\t\tBienvenido usuario: ')
        print('1.Calcular MCD\r\n2.Crear cadena repetitiva \r\n3.Contar cuantas veces aparece una letra')
        print('4.Convertir numero decimal a binario \r\n5.Calcular cuantos digitos tiene un numero \r\n6.Salir')
        opcion = int(input('Seleccione una opcion: '))
        match opcion:
            #case 1:
            #case 2:
            #case 3:
            #case 4:
            case 5:
                digitos = int(input('Ingrese el numero del que desea saber cuantos digitos tiene'))
                print(calc_numeros(digitos))
            case 6:
                print('Gracias por usar el sistema')
                fin_menu = False
            case _:
                print('Esta entrada no existe por favor intentelo de nuevo')


    except ValueError:
        print('Ocurrio un error en el ingreso de datos')
