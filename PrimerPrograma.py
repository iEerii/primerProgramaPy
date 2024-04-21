numerosIngresados = []
for i in range(3):
    numero = int(input("Ingresa un numero: "))
    numerosIngresados.append(numero)

print("los numeros que ingresó son: ", numerosIngresados)

minimo = min(numerosIngresados)
print("El numero pequeño es: ", minimo)

maximo = max(numerosIngresados)
print("El numero mayor es: ", maximo)