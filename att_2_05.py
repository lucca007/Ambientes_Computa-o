'''
5. (GC) O conteúdo GC de uma string de DNA é dado pela porcentagem de
símbolos na string que são 'C' ou 'G'. Por exemplo, o conteúdo de GC de
"AGCTATAG" é de 37,5%. Observe que o complemento reverso de qualquer string
de DNA tem o mesmo conteúdo de GC. Considerando isso, faça um programa que
leia um arquivo FASTA contendo várias identificadores (que começam com o
carácter “>”) e sequências de DNA. O programa deve retornar o identificador da
sequência que possua o maior conteúdo GC seguido do valor do conteúdo GC [5].
Exemplo entrada:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGA
GG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAG
ACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGT
AGGTGGAAT
Saída:
Rosalind_0808
60.919540
'''


sequência_toda={}
nome= None
GC_maior = 0


with open ('arquivo_teste', 'r') as arq:
    for linha in arq:
        linha=linha.strip()
        if linha.startswith(">"):
            nome = linha[1:]
            sequência_toda[nome] = ''
        else:
            sequência_toda[nome] += linha
    


#print(sequência_toda)

for chave, valor in sequência_toda.items():
    total=len(valor)
    GC= valor.count('G') + valor.count('C')
    GC_p= GC/total * 100
    
if GC_p > GC_maior:
    GC_maior= GC_p
    GC_m_nome= chave

    print(GC_m_nome, GC_maior)
    

