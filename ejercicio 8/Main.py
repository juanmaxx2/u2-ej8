from conjunto import Conjunto
if __name__=='__main__':
    cant=int(input('\nIngrese la cantidad de elemtnos del primer conjunto:'))
    a=Conjunto()
    for i in range(cant):
        num=int(input('\nIngrese el numero a agregar:'))
        a.AgregarNum(num)
    
    cant=int(input('\nIngrese la cantidad de elemtnos del segundo conjunto:'))
    b=Conjunto()
    for i in range(cant):
        num=int(input('\nIngrese el numero a agregar:'))
        b.AgregarNum(num)
    
    opcion=None
    while opcion!='d':
        print('\n')
        print('1) Union entre conjunto')
        print('2) Diferencia de conjunto')
        print('3) Ver si son iguales los conjuntos')
        print('4) Salir')
        opcion=input('Ingresar opcion a realizar:')
        
        if opcion=='1':
            c=a.__add__(b)
            print(c)
        
        elif opcion=='2':
            c=a.__sub__(b)
            print(c)
        
        elif opcion=='3':
            if a.__eq__(b):
                print('\nSon iguales')
            else: print('\nNo son iguales')