#Algoritmo: Operadores e Expressões em Python


import math

#Bibliotecas exemplo
print(math.sqrt(81))
print(math.pow(2,2))
print(2 ** 2)
print(divmod(20,6))
print(20//6) #DIV
print(20%6)

#Soma e subtração

print(20+4-6)

#Potência

print(2^4)

#Divisão

print(20/4)

#Precedência de operadores
# a ** 2 + b * 3 % 2 , sendo  que a=6 e b=3
# 6 ** 2 + 3 * 3 % 2

print( 6 ** 2 + 3 * 3 % 2 )

#Operadores lógicos: AND

print(5>= 5 and 4 < 5)
print(5 ==5 and 5 >9)
print(5 == 4 and 5 >= 4)
print(5 == 4 and 5>= 7)

#Operadores lógicos: OR

print("\n")
print(5>= 5 or 4 < 5)
print(5 ==5 or 5 >9)
print(5 == 4 or 5 >= 4)
print(5 == 4 or 5>= 7)


#Operadores lógicos: NOT
print("\n")
print( not 5 == 4)
print( not 5 > 4)

#Operadores relacionais

print(78 > 10)
print(78 < 10)
print(78 >= 10)
print(78 <= 10)
print(78 == 10)
print(78 != 10)

#Operadores de atribuição
x = 90
print(x)

x +=2
print(x)

x -=10
print(x)

x/=10
print(x)
x=20

x//=10
print(x)

x = 20
x%=10
print(x)

x=1000000000
x *=10
print(x)

print(2 + 3 * 5 + 30 // 10)

print(True or False and not True)