x = int(input("coloque número: "))

def recursion (y: int):
    if y==0: return 1
    if y==1: return 1
    return y*(y-1)

print("factorial é", recursion)


