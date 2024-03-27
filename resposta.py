from math import sqrt


#a. Some os números
n1 = 2
n2 = 4
soma = n1+n2
print("A soma de", n1, "e", n2, "é" ,soma)


#b. Multiplique
print(7*4)


#c. Divide
print(9/3)
print(9\
      //3)



#d. Raiz quadrada
print (25**0.5)
print(sqrt(25))
print(25**(1/2))

# e. imprima o resultado de 2**3
print(2**3)



# f. some o quadrado de 3 com 23
print(23+(3**2))

print(
    ((3**2)+23)
)


# g. imprima o resto de 7 elevado a 2 pelo raiz quadrada de 625
print(
    (7**2)%(625**0.5)
    )


# h. retorne o módulo de 11 por 2

print (11 % 2)


# i. retorne o módulo de 749 por 7

print(749%7)


# Ver tamanho de pacote
import sys

def module_size(math):
    try:
        module = __import__(math)
        size = sys.getsizeof(math)
        print(f"The size of the '{math}' module is approximately {size} bytes.")
    except ImportError:
        print(f"Module '{math}' not found.")

# Example usage:
module_size('math')
module_size('random')

