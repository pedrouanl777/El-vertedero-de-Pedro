# Segun google esto se necesita para sacar el interés compuesto (?)
print('Saldo actual')
current = float(input())

print('Adición anual')
adicionAnual = float(input())

print('Años a invertir')
años = int(input())

print('Interés deseado')
interes = float(input())

total = current

for i in range(años):
    total = total + adicionAnual
    total = total + (interes * total / 100)
    print(i)

print('Resultado: $' + str(total)) # Toca practicar con más de estos :B