with open("RGK.pdb") as arquiv:
    linhas = arquiv.readlines()

    list=[]
    list_n=[]
    count=0

    for linha in linhas:
        if linha[0:4] == "ATOM":
           if linha[23:26] != count:
                count = linhas [23:26]
                list.append(linha[17:20])
                
    
    

    print(list)



#     for linha in linhas:
#         if linha[0:4] == "ATOM":
#             list.append(linha[23:26]) 
# print(list)
# print(list_n)


# list_linhas= list.replace(" ","\t")
# print(list_linhas)
# dicionario = dict(zip(list, list_n))

