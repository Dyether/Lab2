from pickle import TRUE

while TRUE:
    opcion = input("digite una opcion: ")
    if(not(opcion.isdigit())):
        print("debe dijitar una opcion entre 1 y 5: ")
        continue
    i = int(opcion)
    if i == 1:
        horas = int(input("¿Cuantas horas trabajaste?:"))
        resultado = horas * 1600
        print("Tu salario actual es de: " + str(resultado))
    elif i == 2:
        nombre = input("Cual es tu nombre?: ")
        print("Bienvenido a la UIA " + nombre.upper())
        print("Bienvenido a la UIA " + nombre.lower())
    elif i == 3:
        edad = int(input("Cuale es tu edad?: "))
        if (edad >= 18):
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
    elif i == 4:
        numero = int(input("Digita un munero entero entre uno y cien: "))
        for a in range(1, numero + 1, 2):
            print(a, end=",")
    elif i == 5:
        print("Gracias por usar mi super mega duper programa blabla.")
    elif i == 6:
        print("Esto es una suma")
        break
