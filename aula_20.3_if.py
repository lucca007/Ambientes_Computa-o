'''
x = 1
y = 2
if y > x :
    print("Condição atendida")


condicao= True
if condicao:
    print("aaaaa")

abc = False
if abc:
    ("Isso aqui não vai imprimir")

print("Mas isso vai")
'''


# Atribuição múltipla
c1,c2,c3,c4,c5 = True, True, True, True, True, 

# Indentação hierárquica
if c1:
    if c2:
        if c3:
            if c4:
                if c5:
                    print ("O nome disso é Indentação hierárquica")


c1,c2,c3,c4,c5 = True, True, False, False, True, 

# Indentação hierárquica
if c1:
    if c2:
        if c3:
            if c4:
                print ("Isso não vai ser impresso")
        if c5: 
            print ("Isso vai ser impresso")
                    

c1,c2,c3,c4,c5 = True, True, False, True, True, 
if c1:
    if c2:
        if c3:
            print("Como eu abri um bloco de código, eu TENHO que colocar alguma coisa aqui")
    if c4:
        if c5:
            print ("Isso vai? Agr Sim!")   