#Algoritmo: Operações com tipos básicos

x=1
y=2

resultado = x + y
print(resultado)
print(type(resultado))

#ponto flutuante
x = 2.2
y = 5.9
resultado = x + y
print(resultado)
print(type(resultado))

# número inteiro com ponto flutuante
a = 2
b = 2.5
operacao=print(a+b)

# Conversão de tipos
e= 10
s = str(e)
print(s)
print(type(s))

# Conversão de float para inteiro
e= 2.5
s = int(e)
print(s)
print(type(s))

# Conversão de inteiro para float
e= 2
s = float(e)
print(s)
print(type(s))

lista = [1, 2, 3, 4, 5]

for item in lista:
    print(item)


print("\n")
elemento = 10
EstaPresente = False
lista = [1, 2, 7, 10, 15, 20, 50]
for item in lista:
 if item == elemento:
  EstaPresente = True

if EstaPresente:
 print("Elemento está na lista!")
else:
 print("Elemento não está na lista!")








print("\n")
def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat

print("O fatorial de {} é {}".format(6, fatorial(6)))




print("Digite seu nome:")
nome = input()
print("Bem-vindo, ", nome)