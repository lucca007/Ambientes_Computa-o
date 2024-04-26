'''
Faça um programa que leia um arquivo FASTA contendo múltiplos
identificadores e sequências. Para cada identificador e sequência o programa deve
criar um arquivo de saída contendo o identificar e sua respectiva sequência. O nome
dos arquivos de saída devem ser iguais aos seus respectivos identificadores,
seguido de “.fasta”
'''

seqs = []
nomes = []

with open ('Rosalind_10', 'r') as arq:
    for linha in arq:
        linha=linha.strip()
        if linha.startswith(">"):
            nome = linha.replace(">","")
            # print(nome)
            nomes.append(nome)
        else:
            seq = linha
            seqs.append(seq)

tuplas = []

for i in range(len(nomes)):
    tuplas.append(tuple((nomes[i], seqs[i])))
print(tuplas)

for tupla in tuplas:
    file_path = f'./{tupla[0]}.fasta'
    with open (file_path, 'w') as file:
        print(f"{tupla[1]}", file=file)

# for tupla in tuplas:
