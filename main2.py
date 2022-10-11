'''



idade= int
peso = float
idade=input("Digite sua idade")
peso=input("Digite seu peso")
print(idade)
print(peso)
print(type(idade))
print(type(peso))

a = float(input('Digite um número: '))
print(type(a))





Salario = ValorPoupanca = RendaPoupanca = ValorFundoRendaFixa = RendaFundo = Meses = 0
RendaPoupanca = 1.02
RendaFundo = 1.05
Salario = float(input("Qual o salário: "))
ValorPoupanca = Salario * RendaPoupanca
print(ValorPoupanca)
Salario = Salario / 3
ValorFundoRendaFixa = Salario * RendaFundo
print(ValorFundoRendaFixa)
while True:
    Meses += 1
    print(f"O valor de investimentos do João é: , {ValorFundoRendaFixa:,.2f}, mês",
Meses)
    if ValorFundoRendaFixa <= ValorPoupanca:
        ValorFundoRendaFixa = ValorFundoRendaFixa * RendaFundo
        continue
    else:
        break





novo_salario= float
salario = float
percentual = int
ano_atual=int(input("Digite o ano atual"))
salario = 1.000
percentual = 1.5/100
novo_salario = salario + percentual * salario
iterador = 2000
while(iterador<=ano_atual):
 percentual = 2 * percentual
 novo_salario= percentual*novo_salario
 iterador = iterador + 1
else:

 print(f'Novo salário = {novo_salario:.2f}')







Salario = ValorPoupanca = RendaPoupanca = ValorFundoRendaFixa = RendaFundo = Meses= 0
RendaPoupanca = 1.02
RendaFundo = 1.05
Salario = float(input("Qual o salário: "))
ValorPoupanca = Salario * RendaPoupanca
print(ValorPoupanca)
Salario = Salario / 3
ValorFundoRendaFixa = Salario * RendaFundo
print(ValorFundoRendaFixa)
while True:
    Meses += 1
    print(f"O valor de investimentos do João é: , {ValorFundoRendaFixa:,.2f}, mês",
Meses)
    if ValorFundoRendaFixa <= ValorPoupanca:
        ValorFundoRendaFixa = ValorFundoRendaFixa * RendaFundo
        continue
    else:
        break


'''

import math

while True:
    numero = int(input("Digite um número: "))
    if numero <= 0:
        print("Fim")
        break
    else:

     print(numero**2)
     print(numero**3)
     raiz = math.sqrt(numero)
     print(f'\nA raiz quadrada de {numero} é {raiz}\n')




