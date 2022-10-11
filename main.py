#Algoritmo Tarefa 001: Idade e peso (IF)

"""
HorasExtras= float (input("Digite as horas extras "))
HorasFaltas= float(input("Digite as faltas"))

Totalminutos =(HorasExtras - (2/3 * HorasFaltas))* 60

print(Totalminutos)

if Totalminutos >= 2401:
    print("Minutos totais:", Totalminutos,"com gratificação de R$ 500,00")
elif Totalminutos >= 1801 and Totalminutos <= 2401 :
    print("Minutos totais:", Totalminutos,"com gratificação de R$ 400,00")
elif Totalminutos >= 1201 and Totalminutos <= 1800 :
    print("Minutos totais:", Totalminutos,"com gratificação de R$ 300,00")
elif Totalminutos >= 600 and Totalminutos <= 1200:
    print("Minutos totais:", Totalminutos, "com gratificação de R$ 200,00")
elif Totalminutos < 600:
    print("Minutos totais:", Totalminutos,"com gratificação de R$ 100,00")


"""

"""
idade= int(input("Digite sua idade"))
peso = float(input("Digite sua idade"))

if idade <20 and peso <= 60 :
    print("Com", idade,"anos e peso de ", peso,"kilos, você está no grau de risco 9 ")
elif idade < 20 and peso > 60 and peso <= 90:
    print("Com", idade,"anos e peso de ", peso,"kilos, você está no grau de risco 8 ")
elif idade < 20 and peso > 90 :
    print("Com", idade,"anos e peso de ", peso,"kilos, você está no grau de risco 7 ")
elif idade >= 20 and idade <= 50 and peso <= 60:
    print("Com", idade,"anos e peso de ", peso,"kilos, você está no grau de risco 6 ")
elif idade >= 20 and idade <= 50 and peso > 60 and peso <= 90:
    print("Com", idade,"anos e peso de ", peso,"kilos, você está no grau de risco 5 ")
elif idade >=20 and idade <= 50 and peso > 60 and peso <= 90:
    print("Com", idade, "anos e peso de ", peso, "kilos, você está no grau de risco 5 ")
elif idade >= 20 and idade <= 50 and peso > 90 :
    print("Com", idade, "anos e peso de ", peso, "kilos, você está no grau de risco 4 ")
elif idade > 50 and  peso <= 60 :
    print("Com", idade, "anos e peso de ", peso, "kilos, você está no grau de risco 3 ")
elif idade > 50 and peso > 60 and peso <= 90:
    print("Com", idade, "anos e peso de ", peso, "kilos, você está no grau de risco 2 ")
elif idade > 50 and peso > 90:
    print("Com", idade, "anos e peso de ", peso, "kilos, você está no grau de risco 1 ")




"""



laco1= 1
laco2= True
laco3= True

while laco1 <= 10 :
    salariominimo = 450
    salarioinicial = 0
    salariofinal = 0
    auxiloialimentacao = 0

    codigo = input("Digite o código do funcionáo:")
    horatrabalhada = float(input("Digite as horas trabalhadas"))

    while laco2:
        categoria = input("Digite a categoria ")
        if categoria == 'A' or categoria == 'G':
            laco2 = False
        else:
            print("As categorias possíveis são 0 a 6, digite novamente.....")
            continue
        break

    while laco3:
        turno = input("Digite o turno:")
        if Turno == 'M' or Turno =='V' or Turno == 'N':
            laco3 = False
        else:
            print("Os turnos possíveis são: V ou M ou N, digite novamente......")
            continue
    break

if categoria == "G" and turno == "N":
    valorhora = salariominimo * 0.18
    salarioinicial = horatrabalhada * valorhora
    if salarioinicial <= 300:
        auxiloialimentacao = salarioinicial * 0.20
        salariofinal = salarioinicial + auxiloialimentacao
    elif salarioinicial > 300 and salarioinicial <=600 :
        auxiloialimentacao = salarioinicial * 0.15
        salariofinal = salarioinicial + auxiloialimentacao
    else:
        auxiloialimentacao = salarioinicial * 0.05
        salariofinal = salarioinicial + auxiloialimentacao


if categoria  == "G" and turno =="M" or turno =="V" :
    valorhora = salariominimo * 0.15
    salarioinicial = horatrabalhada * valorhora
    if salarioinicial <= 300:
        auxiloialimentacao = salarioinicial * 0.20
        salariofinal = salarioinicial + auxiloialimentacao
    elif salarioinicial > 300 and salarioinicial <= 600:
        auxiloialimentacao = salarioinicial * 0.15
        salariofinal = salarioinicial + auxiloialimentacao
    else:
        auxiloialimentacao = salarioinicial * 0.05
        salariofinal = salarioinicial + auxiloialimentacao

if categoria  == "A" and turno =="M" or turno =="V" :
    valorhora = salariominimo * 0.13
    salarioinicial = horatrabalhada * valorhora
    if salarioinicial <= 300:
        auxiloialimentacao = salarioinicial * 0.20
        salariofinal = salarioinicial + auxiloialimentacao
    elif salarioinicial > 300 and salarioinicial <= 600:
        auxiloialimentacao = salarioinicial * 0.15
        salariofinal = salarioinicial + auxiloialimentacao
    else:
        auxiloialimentacao = salarioinicial * 0.05
        salariofinal = salarioinicial + auxiloialimentacao


if categoria  == "A" and turno =="M" or turno == "V" :
    valorhora = salariominimo * 0.10
    salarioinicial = horatrabalhada * valorhora
    if salarioinicial <= 300:
        auxiloialimentacao = salarioinicial * 0.20
        salariofinal = salarioinicial + auxiloialimentacao
    elif salarioinicial > 300 and salarioinicial <= 600:
        auxiloialimentacao = salarioinicial * 0.15
        salariofinal = salarioinicial + auxiloialimentacao
    else:
        auxiloialimentacao = salarioinicial * 0.05
        salariofinal = salarioinicial + auxiloialimentacao

print("Código",codigo,"Horas trabalhadas ",horatrabalhada,"Categoria",categoria,"Turno",turno)
print("Valor da hora",valorhora,"Salário inicial", salarioinicial,"Auxilio alimentação", auxiloialimentacao,"Salário final ", salariofinal )
print("Número do laço principal:",laco1)
laco1= laco1 + 1
laco2 = True
laco3 = True
