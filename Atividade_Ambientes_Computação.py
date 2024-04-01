# 1. Crie um programa em Python que imprima a mensagem na tela: “Hello world!”.
print("Hello world!")

# 2. Escreva um programa que:
# a. Some os números 2 e 2;
# b. Multiplique os números 7 e 4;
# c. Divida o número 9 por 3;
a = 2+2
b = 7*4
c=9/3

print(a,b,c)

# 3. Escreva um programa que:
# a. Encontre a raiz quadrada de 25;
# b. Imprima o resultado de 2³;
# c. Some o quadrado de 3 com 2³;
# d. Imprima o resto de 7² pela raiz quadrada de 625;
a3= 25**0.5
b3=2**3
c3=(3**2)+(2**3)
d3= (7**2) % (625**0.5)

print(a3, b3, c3, d3)


# 4. Escreva um programa que receba duas variáveis (a e b), com valores 10 e 7, respectivamente,
# e determine se:
# a. a > b
# b. (a * a) > b²
# c. (b * a) <= a²
# d. 2+5(a * a)-10 > a*b²

a4=10
b4=7

if a4>b4:
    print(a4, "é maior que", b4)

if (a4**2)>b4**2:
    print(a4, "ao quadrado é maior que", b4,"ao quadrado")
else:
    print(a4, "ao quadrado não é maior que", b4,"ao quadrado")

if (b4 * a4)<= a4**2:
    print(b4,"multiplicado por", a4, "é menor ou igual a", a4, "ao quadrado")
else:
    print(b4,"multiplicado por", a4, "é maior", a4, "ao quadrado")

if (2+5*(a4**2)-10) > a4*(b4**2):
    print("(2+5(10**2)-10) é maior que 10*49")
else:
    print ("(2+5(10**2)-10) não é maior que 10*49")





# 5. Escreva um programa que receba três variáveis (a, b e c), com valores 10, 14 e 7,
# respectivamente, e determine se:
# a) a > b and a*2 < c
# b) a*5 < c**2 or a ==b
# c) not(b >= c*2 and a <= c+3)
# d) (a**2 < c **(1/2) and (a>b+c))

a5=10
b5=14
c5=7

result5_a= a5>b5 and a5**2<c5
result5_b= a5**5<c5**2 or a5==b5
result5_c= not (b5 >= c5**2 and a5 <= c5+3)
result5_d= (a5**2 < c5 **(1/2) and (a5>b5+c5))

print(result5_a,result5_b,result5_c, result5_d)



# 6. Agora, escreva um programa que receba três variáveis (a, b e c), com valores 18, 4 e 3,
# respectivamente, e determine se:
# a) (a+b+c < a*c*b) or (1==1)
# b) (a+b+c < a*c*b) and (1==1)
# c) (a>a<b) and (not(a > b < a))
# d) (a>a<b) or (not(a > b < a))

a=18
b=4
c=3

result6_a = (a+b+c < a*c*b) or (1==1)
result6_b =  (a+b+c < a*c*b) and (1==1)
result6_c = (a>a<b) and (not(a > b < a))
result6_d = (a>a<b) or (not(a > b < a))


print(result6_a, result6_b, result6_c, result6_d)



# 7. Escreva um programa que receba três variáveis (a, b e c), com valores -4, 12 e 79,
# respectivamente, e determine se:
# a) ((a>a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1))
# b) ((a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1)) and
# (not(1>a**(1/2)))

a=-4
b=12
c=79

result7_a= ((a>a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1))
print(result7_a)

if a>=0:
    result7_b= ((a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1)) and (not(1>a**(1/2)))
    print(result7_b)
else:
    a = (a**2)**0.5
    result7_b_= ((a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1)) and (not(1>a**(1/2)))    
    print("numero negativo não tem raiz, mas se quiser fazer com o módulo do número, esse é o resultado:", result7_b_)


# 8. Desenvolva um programa que um valor em segundos e, em seguida, imprima quantas horas,
# minutos e segundos esse valor representa. Teste com o valor 300.
sec= int (input("coloque o valor em segundos:"))

horas= sec // 3600
sec_restante= sec% 3600
minutos= sec_restante //60
sec_restante_final = sec_restante % 60

print(horas, "Horas",minutos, "minutos",sec_restante_final, "segundos")

# 9. Escreva um programa que receba dois números e mostre qual deles é o maior. Teste com os
# valores 0.918259123 e 0.012412.

x =float(input("coloque primeiro numero: "))
y= float(input("coloque segundo numero: "))

if x>y:
    print("primeiro valor maior que o segundo")
elif x<y:
    print("primeiro valor menor que o segundo")
else:
    print("valores iguais")

# 10. Desenvolva um script que calcule o fatorial de um número. Teste com o número 5.

x= int(input("Insira o número para ser calculado o módulo:"))

def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fatorial (n-1)

print("O fatorial de", x, "é", fatorial(x))


# 11. Escreva um programa em que calcule o diâmetro, a circunferência e a área de um círculo.
# O programa deve receber como entrada uma variável com o valor do raio. Considere Pi como
# 3,14. Teste com o valor 10.

pi=3.14
r = int(input("insira o valor do raio do círculo:"))

diametro = 2*r
circunferência = 2*r*pi
área= pi*(r**2)

print("O diametro, circunferencia e área são, respectivamente:", diametro,circunferência,área)




# 12. Escreva um programa que calcule o resultado de uma equação de segundo grau. Realize
# controle de exceções para verificar se delta é menor que zero.


a= int(input("a coloque o valor do coeficiente associado a variável independete:"))
b= int(input("b coloque o valor do coeficiente associado a variável dependete:"))
c= int(input("c coloque o valor da constante"))
       
if a==0:
    print("a não pode ser igual a 0")
else:
    delta= (b**2) - 4*a*c
    if delta>0:
        print("essa equação possui duas raízes reais distintas")
        x1= (-b - delta**0.5)/(2*a)
        x2= (-b + delta**0.5)/(2*a)
        print("as raízes da equação são",x1, "e", x2)
    elif delta==0:
        print("possui duas raízes reais iguais ou uma raiz real dupla")
        x1= (-b /(2*a))
        print("raiz real da equação",x1)
    else:
        print("uma equação em que Δ < 0 não possui raízes reais, mas sim, raízes complexas")
        raíz_real = -b / (2*a)
        raíz_imaginaria = (-delta)**0.5 / (2*a)
        print("As raízes da equação quadrática são complexas:")
        print("x1 =", raíz_real, "+", raíz_imaginaria, "i")
        print("x2 =", raíz_real, "-", raíz_imaginaria, "i")




# 13. Escreva um programa que receba um número inteiro maior que zero e retorne se ele é par
# ou ímpar.

x= (input("coloque número:"))

if '.' in x:
    print ("Número é um número de ponto flutuante, não pode ser classificado como par ou ímpar.")
else:
    x=int(x)
    if x<= 0:
        print("número negativo ou igual a 0 não rola")
    else:
        if x%2==0:
            print("número par")
        else:
            print("número impar")



# Para os exercícios 14-17, considere a seguinte lista:
numeros = [5,15,3,67,8,9,1,7,4,100,97,47,2,72]

# 14. Escreva um programa em Python que imprima o primeiro e o último item.
print("Primeiro item:", numeros[0])
print("Ultimo item:", numeros[-1])
# 15. Escreva um programa que retorne o tamanho da lista.
tamanho=len(numeros)
print(tamanho)
# 16. Escreva um programa em Python que retorne o maior elemento da lista e sua posição.
maior=max(numeros)
posição_maior= numeros.index(maior)
print("maior elemento e sua posição", maior, posição_maior)
# 17. Escreva um programa em Python que retorne o menor elemento da lista e sua posição.
menor=min(numeros)
posição_menor=numeros.index(menor)
print("maior elemento e sua posição", menor, posição_menor)




# Para os exercícios 18-20, considere a seguinte variável:
# mensagem = "Eu amo Python"

# 18. Escreva um programa em Python que retorne a primeira e a última letra da variável
# “mensagem”.
mensagem= "Eu amo Python"
primeiro=mensagem[0]
ultimo=mensagem[-1]
print("primeira e ultima letra:", primeiro, ultimo)

# 19. Escreva um programa que transforme o texto apresentado em uma lista de palavras.
lista_mensagem= mensagem.split()
print("lista de palavra", lista_mensagem)

# 20. Escreva um programa que extraia do texto apenas a palavra Python


for palavra in lista_mensagem:
    if palavra == "Python":
        print("Palavra na mensagem encontrada: ", palavra)   
        if "Python" in lista_mensagem:
            posição_Python= lista_mensagem.index("Python")
            print("posição da palavra Python na lista:", posição_Python)
        break
else:
    print("Não tem Python na mensagem")