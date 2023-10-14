#Obtenemos la cantidad de personas a ser evaluadas
#personas = int(input( "Ingrese cantidad de personas a evaluar: "))

#opcion 2 para evitar que se repita el ciclo
resp= 'S'
while(resp== 'S' or resp== 's'):

    print("Calculo de IMC-HTA")
    print("Bienvenido!, conozca su indice de masa corporal y presion arterial")
#Se puede colocar otra opcion para verificar la cantidad de personas que sea mayor a 0.
#while personas > 0:
    #Se pide el nombre de la persona a analizar
    n = input("Cual es su nombre? ")
    #Tambien le pedimos su apellido para mas formalidad
    ap = input("Cual es su apellido? ") 
    #Se pide edad, se pone como entero
    e = int(input("Cuantos años tiene? "))
    #como la altura es en metros, se tiene que poner como flotante
    a = float(input ("Cual es su altura en metros? "))
    #se especifica que la estatura es la altura dada en metros
    est = a
    #La masa en kg si tiene decimales, es flotnte 
    m = float (input("Cuanto pesa? "))
    #El valor de presion sis. se coloca como int por que es entero
    pas = int (input("Introduzca su presion sistolica (valor superior): "))       
    #Lo mismo para valor diast., es un entero
    pad = int(input("Introduzca su presion diastolica (valor inferior): "))

    print("-----------------------------------------------")
    #Se coloca como encabezado para separar los datos ingresados de los resultados obtenidos
    print(("Resultados del analisis de: " 
    + n  +("-")+ ap)) 
    #calculo del PAM, pas+2pad/3 
    PA = (pas + pad*2)/3  
    print ("Su presion arterial media es: ",float(PA))
    #Si PA es menor o igual a 105 le decimos que es presion normal, si es mayor le decimos que es HiperPA
    if(PA < 105):
        print("Usted tiene valores de presion arterial normales")
    else:
        print("Cuidado, usted padece valores altos de presion arterial, " +
        "acuda a revisión médica para su valoracion")    
    #Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
    IMC = m / est**2
    #Le decimos si es menor o mayor de edad, si es menor a 18 es menor, si no es mayor edad
    if(e < 18):
        print("Usted es menor de edad, aun se encuentra en desarrollo")
    if (e >= 18 and e <= 26):
        print("Usted esta en etapa de adulto joven")
    if (e >= 27 and e <=59):
        print("Usted esta en la etapa de adultez")
    else:
        print("Usted es una persona de edad avanzada")
    #Se imprime el IMC
    print("Su IMC es: " + str(IMC))
    print("Usted presenta: ")
    #Hacemos las distintas validaciones
    if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Peso Saludable")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")

    print("nos vemos pronto " + n)
    #Por cada persona a la que le pedimos los datos debemos restarle una (Porque ya la recorrimos)
    #si no el ciclo se vuelve infinito (opcion 1)
    #personas = personas - 1
    print("-------------------------------------------")
    #se coloca la variable resp con su respectivo input para que decida usuario cerrar ciclo
    print("Desea analizar de nuevo? Si <S> No <N>")
    resp=input()