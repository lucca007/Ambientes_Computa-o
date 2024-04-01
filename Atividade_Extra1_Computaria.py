
# Parte 1 – Fundamentos do Python (1 ponto extra)
# 1. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
x=int(input("número"))
print("o número informado foi:", x)

# 2. Faça um Programa que peça dois números e imprima a soma.
x=int(input("número"))
y=int(input("número"))

print(x+y)

# 3. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
x=int(input("número 1 nota"))
y=int(input("número 2 nota"))
z=int(input("número 3 nota"))
w=int(input("número 4 nota"))

print((x+y+w+z)/4)

# 4. Faça um Programa que converta metros para centímetros.
x=int(input("número metros"))

print(x*100, "centimetros")


# 5. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
x=int(input("número raio circulo"))

area= 3.14 *(x**2)
print(area)

# 6. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o
# usuário.

x=int(input("número lado quadrado: "))
area_q= x**2

print("o dobro da area do quadrado"(area_q)*2)

# 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
x=int(input("número que vc ganha por hora: "))
y=int(input("número horas trabalhadas: "))

salario= x*y

print(salario)

# 8. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em
# graus Celsius.
# o C = 5 * ((F-32) / 9).
F=int(input("número temperatura F: "))
C= 5*((F-32)/9)
print(C)

# 9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
x=int(input("número temperatura C:"))

F= ((9/5)*x)+32
print(F)

# 10. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.
x=int(input("número inteiro"))
y=int(input("segundo número inteiro"))
z=float(input("número real"))

r_a= (x**2)*(y/2)
r_b= (x*3)+z
r_c= z**3

print(r_a, r_b, r_c)

# 11. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

altura=int(input("número altura: "))

peso_ideal=(72.7*altura) - 58

print(peso_ideal)

# 12. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7

h=int(input("número altura: "))
g= input("qual seu gênero, homem ou mulher : ")

if g.lower()=="homem":
    a=  (72.7*h) - 58
    print("peso ideal p/ homem", a)
else:
    b= (62.1*h) - 44.7
    print("peso ideal p/ mulher", b)

# 13. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
# diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
# regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
# excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule
# o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor
# da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso=int(input("peso de peixes dessa vez: "))

if peso > 50:
    excesso = peso - 50
    multa= excesso*4
    print("vc vai ter que pagar", multa,"reais por excesso", excesso)

# 14. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

x=int(input("quanto vc ganha por hora: "))
y=int(input("horas trabalhadas: "))

salario_bruto= x*y
ir=salario_bruto*0.11
inss=salario_bruto*0.08
sindicato=salario_bruto*0.05
salario_liquido= salario_bruto-(ir, inss, sindicato)

print("salario bruto, quanto pagou INSS, quanto pagou sindicato, salario liquido (respectivamente)", salario_bruto, inss, sindicato, salario_liquido)
print("vc pagou para o INSS, IR, e sindicato esses valores (respectivamente)", inss, ir, sindicato)


# 15. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
# área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
# tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
# tinta a serem compradas e o preço total.

x=float(input("tamanho em metros quadrados: "))

litros=x/3

latas= litros/18
if latas%18 != 0:
    latas=latas+1

preço=latas*80

print("latas necessarios e preço a pagar", latas, preço)


# 16. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
# área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a
# tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# o Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3
# situações:
# o comprar apenas latas de 18 litros;
# o comprar apenas galões de 3,6 litros;
# o misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
# sempre arredonde os valores para cima, isto é, considere latas cheias

x=float(input("tamanho em metros quadrados: "))

litros=x/6

latas= litros/18
if latas%18 != 0:
    latas=latas+1

galao= litros/3.6
if galao%3.6 != 0:
    galao=galao+1

latas_p= latas*80
galao_p= galao*25

print("quantidade de tinta a ser comprada", litros, "litros")
print("preço se comprar apenas latas", latas_p)
print("preço se comprar apenas galoes", galao_p)


litros= x/(6*1.1)

latas_necessarias= litros//18
resto= litros%18
galoes_necessarios= resto/3.6
if galoes_necessarios%3.6 != 0:
    galoes_necessarios=galoes_necessarios+1

preço_total= (latas_necessarias*80)+(galoes_necessarios*25)

print("se misturar galoes e latas com 10 por cento de folga, o preço final vai ser de", preço_total)