
x = int(input("coloque número: "))

def a (y: int):
    if y==0: return 1
    if y==1: return 1
    else:
        return y*(a(y-1))

result = a(x)
print("fatorial é", result)




x = int(input("coloque número: "))

resultb = 1
for i in range(1, x+1):
    resultb *= i

print("aaa", resultb)



result= range(1,10)


print (result)
