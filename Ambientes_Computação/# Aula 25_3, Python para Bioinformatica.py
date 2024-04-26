# Aula 25_3, Python para Bioinformatica

'''
i=0

while i<8:
    print(i)
    i += 1


for x in [1,2,3,4,5,6,7]:
    print (x)




# Range: 
# 1 argumento = total
# 2 argumentos = inicio e fim
# 3 argumentos = inicio, fim, passo

um = range(3)
dois = range(1,3)
tres = range(0,10,2)

for i in um:
    print(i, end=".")
print("\n")

for i in dois:
    print(i, end=".")
print("\n")


for i in tres:
    print(i, end=".")
print("\n")


for i in range (2, 10, 2):
    print (i/10, end=",")


for x in range (1,10,2):
    x /=10
    print(x,end=',')


coisas=["abacate","banana","canela"]

for i in coisas:
    print(i)

for a in range(len(coisas)):
    print(a+1, coisas[a])


for b in range(len(coisas)):
    cont = b+1
    print(cont, coisas[b])
'''


'''
lista = range(29)

for x in lista:
    print(x, end=",")
print('\nFIM')


ll = range(10)

for i in ll:
    if i % 2 == 0:
        print(i,end=",")



ll = range(10)

for i in ll:
    if i %2==1:
        print(i)





# \n é pra dar um enter na linha, é uma quebra de linha
ll = range (100)

print("Começo números pares")
for x in ll:
    if x%2==0:
        print(x)
print('\nFIM')

print("\n\n\n\n\n\n\nComeço números ímpares")
for x in ll:
    if x%2==1:
        print(x)
print('\nFIM')


print("\n\n\n\n\n\n\nComeço múltiplos de 7")
for x in ll:
    if x%7==0 and x!=0:
            print(x)
print('\nFIM')

'''
x = int(input("coloque seu número:"))
for x in range (10):
    print(x*x)+(x*(x-1))
