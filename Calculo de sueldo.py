#Se pide el nombre de la persona a analizar
n = input("Su nombre por favor: ")
#Se pide cantidad de bloque pegado
bp = int(input("Cantidad de bloques pegados: "))
#Se pide cantidad de bloque que se quebro
bq = int(input("Cantidad de bloques desperdiciados: "))
#Se solicita el monto gastado en la tiendita
gt = int(input("Ingrese monto gastado en tienda de alimentos: "))

bp=bp*3
bq=bq*-5
gt=gt*-1
#Calculo del sueldo del dia se realiza sumando las variables
SAL=bp+bq+gt   
#Se le imprime el resultado de su salario para que se awuite
print("Su salario en pesos del dia de hoy es de: ")
print (SAL)