def main():
    number = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    numberstr= str(number)
    if len(numberstr)>6:
        print('Too long')
    else:
     if number >0:
        reverso= numberstr[len(numberstr)::-1]
        print(reverso)
     else:
        negativo= numberstr[0]
        reverso= numberstr[len(numberstr):0:-1]
        reversaneg= negativo + reverso
        print(reversaneg)  
    

if __name__=='__main__':
    main()
