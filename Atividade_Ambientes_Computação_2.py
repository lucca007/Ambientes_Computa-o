'''
# Bioinformatics Stronghold
# 1. (DNA) Faça um programa que leia um arquivo contendo uma string de DNA com
# o tamanho de até 1000 nucleotídeos. O programa deve retornar 4 inteiros
# separados por espaços sendo eles a quantidade de ocorrências de 'A', 'C', 'G', and
# 'T' respectivamente [1].
# Exemplo entrada:
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Saída:
# 20 12 17 21

x= input("arquivo de texto com nucleotídeos:")

ATCG= {'A': 0, 'T': 0, 'C':0, 'G':0}

for nucleotideos in x:
    if nucleotideos in ATCG:
        ATCG[nucleotideos]+=1

print(ATCG['A'], ATCG['C'], ATCG['G'], ATCG['T'])


# 2. (RNA) Faça um programa que leia um arquivo contendo uma string de DNA. O
# programa deve retornar uma string que corresponda ao RNA transcrito do DNA
# informado, substituindo os “T”s por “U”s [2].
# Exemplo entrada:
# GATGGAACTTGACTACGTAAATT
# Saída:
# GAUGGAACUUGACUACGUAAAUU

x= input("arquivo de texto com nucleotídeos DNA:")

# DNA= ['A', 'T', 'C', 'G']
# RNA= ['U', 'A', 'G', 'C']

RNA=x.replace('A', 'U').replace('T', 'A').replace('C','X').replace('G', 'C').replace('X', 'G')

print(RNA)


# 3. (REVC) Faça um programa que leia um arquivo contendo uma string de DNA. O
# programa deve retornar uma string que corresponda ao DNA complementar (cDNA)
# do DNA informado [3].
# Exemplo entrada:
# AAAACCCGGT
# Saída:
# ACCGGGTTTT

x= input("arquivo de texto com nucleotídeos DNA:")

# DNA= ['A', 'T', 'C', 'G']
# RNA= ['U', 'A', 'G', 'C']

DNAc=x.replace('A', 'Y').replace('T', 'A').replace('C','X').replace('G', 'C').replace('X', 'G').replace('Y', 'T')

DNAc_inverso= DNAc[::-1]

print(DNAc_inverso)


# 4. (FIB) A sequência de Fibonacci pode ser utilizada para estimar a população de
# coelhos a partir de uma quantidade de meses. Considerando isso. faça um
# programa que leia um arquivo contendo dois inteiros (n e k) separados por espaço,
# onde n corresponde a quantidade de meses e k corresponde a quantidade de pares
# de filhotes de coelhos que cada casal (par) de coelhos adultos conseguem gerar por
# mês (ao invés de 1 par, como é normalmente na sequência de Fibonacci). Além
# disso, os coelhos filhotes demoram 1 mês para se tornarem adultos e capazes de se
# reproduzir. Sendo assim, o programa deve retornar o total de pares de coelhos
# depois de n meses, considerando inicialmente que existem 1 par de coelhos
# filhotes no primeiro mês [4].
# Exemplo entrada:
# 5 3
# Saída:
# 19






# 5. (GC) O conteúdo GC de uma string de DNA é dado pela porcentagem de
# símbolos na string que são 'C' ou 'G'. Por exemplo, o conteúdo de GC de
# "AGCTATAG" é de 37,5%. Observe que o complemento reverso de qualquer string
# de DNA tem o mesmo conteúdo de GC. Considerando isso, faça um programa que
# leia um arquivo FASTA contendo várias identificadores (que começam com o
# carácter “>”) e sequências de DNA. O programa deve retornar o identificador da
# sequência que possua o maior conteúdo GC seguido do valor do conteúdo GC [5].
# Exemplo entrada:
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGA
# GG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAG
# ACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGT
# AGGTGGAAT
# Saída:
# Rosalind_0808
# 60.919540

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








# 6. (HAMM) A distância de Hamming (dH) entre duas cadeias com o mesmo
# comprimento é o número mínimo de substituições de símbolos necessárias para
# transformar uma cadeia na outra. Sendo assim, faça um programa que leia um
# arquivo contendo 2 cadeias de DNA s e t de tamanho idêntico. O programa deve
# retornar a distância de Hamming entre s e t, denotada por dH(s,t), onde dH(s,t) é o
# número de símbolos correspondentes que diferem em s e t [6].
# Exemplo entrada:
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# Saída:
# 7
# 7. (PROT) Os 20 aminoácidos de ocorrência comum são abreviados usando 20
# letras do alfabeto inglês (todas as letras, exceto B, J, O, U, X e Z). As cadeias de
# proteínas são construídas a partir desses 20 símbolos. Doravante, o termo string
# genético irá incorporar cadeias de proteínas junto com strings de DNA e strings de
# RNA.
# A tabela de codificação de RNA determina os detalhes relativos à codificação de
# codões específicos no alfabeto de aminoácidos. Sendo assim, faça um programa
# que leia um arquivo contendo uma string de RNA (mRNA). O programa deve
# retornar uma string que corresponda a sequência proteica codificada do mRNA
# informado [7].
# Exemplo entrada:
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
# Saída:
# MAMAPRTEINSTRING


codon_to_amino_acid = {
    "UUU": "F",  # Phenylalanine
    "UUC": "F",  # Phenylalanine
    "UUA": "L",  # Leucine
    "UUG": "L",  # Leucine
    "CUU": "L",  # Leucine
    "CUC": "L",  # Leucine
    "CUA": "L",  # Leucine
    "CUG": "L",  # Leucine
    "AUU": "I",  # Isoleucine
    "AUC": "I",  # Isoleucine
    "AUA": "I",  # Isoleucine
    "AUG": "M",  # Methionine
    "GUU": "V",  # Valine
    "GUC": "V",  # Valine
    "GUA": "V",  # Valine
    "GUG": "V",  # Valine
    "UCU": "S",  # Serine
    "UCC": "S",  # Serine
    "UCA": "S",  # Serine
    "UCG": "S",  # Serine
    "CCU": "P",  # Proline
    "CCC": "P",  # Proline
    "CCA": "P",  # Proline
    "CCG": "P",  # Proline
    "ACU": "T",  # Threonine
    "ACC": "T",  # Threonine
    "ACA": "T",  # Threonine
    "ACG": "T",  # Threonine
    "GCU": "A",  # Alanine
    "GCC": "A",  # Alanine
    "GCA": "A",  # Alanine
    "GCG": "A",  # Alanine
    "UAU": "Y",  # Tyrosine
    "UAC": "Y",  # Tyrosine
    "UAA": "*",  # Stop
    "UAG": "*",  # Stop
    "CAU": "H",  # Histidine
    "CAC": "H",  # Histidine
    "CAA": "Q",  # Glutamine
    "CAG": "Q",  # Glutamine
    "AAU": "N",  # Asparagine
    "AAC": "N",  # Asparagine
    "AAA": "K",  # Lysine
    "AAG": "K",  # Lysine
    "GAU": "D",  # Aspartic Acid
    "GAC": "D",  # Aspartic Acid
    "GAA": "E",  # Glutamic Acid
    "GAG": "E",  # Glutamic Acid
    "UGU": "C",  # Cysteine
    "UGC": "C",  # Cysteine
    "UGA": "*",  # Stop
    "UGG": "W",  # Tryptophan
    "CGU": "R",  # Arginine
    "CGC": "R",  # Arginine
    "CGA": "R",  # Arginine
    "CGG": "R",  # Arginine
    "AGU": "S",  # Serine
    "AGC": "S",  # Serine
    "AGA": "R",  # Arginine
    "AGG": "R",  # Arginine
    "GGU": "G",  # Glycine
    "GGC": "G",  # Glycine
    "GGA": "G",  # Glycine
    "GGG": "G",  # Glycine
}

x= input("Sequencia de mRNA:")
codons= [x[y:y+3] for y in range(0, len(x), 3)]
print(codons)

amino=[]

for i in codons:
    if i in codon_to_amino_acid:
        amino.append(codon_to_amino_acid[i])

print("".join(amino))

        
# 8. (SUBS) Faça um programa que leia um arquivo contendo uma string de DNA s e
# outra p. O programa deve retornar todas as posições (começando e 0) ao qual foi
# encontrado p em s, separadas por espaços [8].
# Exemplo entrada:
# GATATATGCATATACTT
# ATAT
# Saída:
# 2 4 10

y = "ATAT"
x = "GATATATGCATATACTT"
z=[]

for i in range(len(x)):
    if x[i:i+4] == y:
        z.append(i+1)

print(z)



# 9. (SPLC) Após de identificar os exons e os introns de uma string de RNA,
# precisamos apenas deletar os introns e concatenar os exons para formar uma nova
# string pronta para a tradução. Considerando isso, faça um programa que leia um
# arquivo FASTA contendo no primeiro identificador uma cadeia de DNA s seguida de
# um coleção de substrings de s que atuam como introns. O programa deve retornar o
# uma sequência de aminoácidos resultante da transcrição e tradução dos exons de s
# [9].
# Exemplo entrada:
# >Rosalind_10
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
# >Rosalind_12
# ATCGGTCGAA
# >Rosalind_15
# ATCGGTCGAGCGTGT
# Saída:
# MVYIADKQHVASREAYGHMFKVCA
# Bioinformatics Textbook Track

codon_to_amino_acid = {
    "UUU": "F",  # Phenylalanine
    "UUC": "F",  # Phenylalanine
    "UUA": "L",  # Leucine
    "UUG": "L",  # Leucine
    "CUU": "L",  # Leucine
    "CUC": "L",  # Leucine
    "CUA": "L",  # Leucine
    "CUG": "L",  # Leucine
    "AUU": "I",  # Isoleucine
    "AUC": "I",  # Isoleucine
    "AUA": "I",  # Isoleucine
    "AUG": "M",  # Methionine
    "GUU": "V",  # Valine
    "GUC": "V",  # Valine
    "GUA": "V",  # Valine
    "GUG": "V",  # Valine
    "UCU": "S",  # Serine
    "UCC": "S",  # Serine
    "UCA": "S",  # Serine
    "UCG": "S",  # Serine
    "CCU": "P",  # Proline
    "CCC": "P",  # Proline
    "CCA": "P",  # Proline
    "CCG": "P",  # Proline
    "ACU": "T",  # Threonine
    "ACC": "T",  # Threonine
    "ACA": "T",  # Threonine
    "ACG": "T",  # Threonine
    "GCU": "A",  # Alanine
    "GCC": "A",  # Alanine
    "GCA": "A",  # Alanine
    "GCG": "A",  # Alanine
    "UAU": "Y",  # Tyrosine
    "UAC": "Y",  # Tyrosine
    "UAA": "*",  # Stop
    "UAG": "*",  # Stop
    "CAU": "H",  # Histidine
    "CAC": "H",  # Histidine
    "CAA": "Q",  # Glutamine
    "CAG": "Q",  # Glutamine
    "AAU": "N",  # Asparagine
    "AAC": "N",  # Asparagine
    "AAA": "K",  # Lysine
    "AAG": "K",  # Lysine
    "GAU": "D",  # Aspartic Acid
    "GAC": "D",  # Aspartic Acid
    "GAA": "E",  # Glutamic Acid
    "GAG": "E",  # Glutamic Acid
    "UGU": "C",  # Cysteine
    "UGC": "C",  # Cysteine
    "UGA": "*",  # Stop
    "UGG": "W",  # Tryptophan
    "CGU": "R",  # Arginine
    "CGC": "R",  # Arginine
    "CGA": "R",  # Arginine
    "CGG": "R",  # Arginine
    "AGU": "S",  # Serine
    "AGC": "S",  # Serine
    "AGA": "R",  # Arginine
    "AGG": "R",  # Arginine
    "GGU": "G",  # Glycine
    "GGC": "G",  # Glycine
    "GGA": "G",  # Glycine
    "GGG": "G",  # Glycine
}

x="ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG"
introns=["ATCGGTCGAA", 'ATCGGTCGAGCGTGT']

for intron in introns:
    x = x.replace(intron, "")

x = x.replace('T', 'U')

codons = []
amino = []

for i in range(0, len(x), 3):
     codons.append(x[i:i+3])

for c in codons:
     if c in codon_to_amino_acid:
          amino.append(codon_to_amino_acid[c])


print(amino)


# 10. (BA1A) Podemos dizer que um padrão p é o mais frequente k-mer (onde k é o
# tamanho de p) em um texto t se a quantidade de p em t for maior que todos os k-
# mers. Por exemplo, "ACTAT" é um 5-mer mais freqüente em
# "AAACTATACACTATAACTATT", e "ATA" é um 3-mer mais freqüente de
# "CGATATATCCATAG". Considerando isso, faça um programa que leia um arquivo
# contendo uma string de DNA s seguida de um inteiro k. O programa deve retornar
# todos os k-mers mais frequentes em s, separados por espaço [10].
# Exemplo entrada:
# ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4
# Saída:
# CATG GCAT
# Classic Bioinformatics

x = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
km = 4

kmer = (x[i:i+km] for i in range(len(x) - km + 1))
kmer = list(kmer)

contagem = {}

for i in kmer:
    contagem[i] = contagem.get(i, 0) + 1

chave_maxima = []
valor_maximo = (0)


for chave, valor in contagem.items():
    if valor > valor_maximo:
        chave_maxima = [chave]
        valor_maximo = valor
    elif valor == valor_maximo:
        chave_maxima.append(chave)

print(chave_maxima)


# 11. Faça o programa que leia o resultado de alinhamento entre duas sequências
# com BLAST e retorne a identidade (em porcentagem). Dica: copie a tabela abaixo e
# cole em um arquivo chamado “resultado.txt”; leia o arquivo manualmente e
# identifique qual linha armazena o valor de identidade; depois crie um programa que
# leia e imprima na tela apenas esse valor.
# Query= sp|P52407|E13B_HEVBR Glucan endo-1,3-beta-glucosidase, basic
# vacuolar isoform OS=Hevea brasiliensis OX=3981 GN=HGN1 PE=1 SV=2
# Length=374
# Subject= sp|Q9SE50|BGL18_ARATH Beta-D-glucopyranosyl abscisate
# beta-glucosidase OS=Arabidopsis thaliana OX=3702 GN=BGLU18 PE=1 SV=2
# Length=528
# Score = 25.0 bits (53), Expect = 0.005, Method: Compositional matrix adjust.
# Identities = 26/126 (21%), Positives = 51/126 (40%), Gaps = 18/126 (14%)
# Query 233 FTSPSVVVWDGQR--GYK---NLFDATLDALYSALE------RASGGSLEVVVSESGWPS 281
# +T+ S+V WD + GYK F+ LD L + + G EV+++E+G+
# Sbjct 368 WTTDSLVDWDSKSVDGYKIGSKPFNGKLDVYSKGLRYLLKYIKDNYGDPEVIIAENGYGE 427
# Query 282 AGA-------FAATFDNGRTYLSNLIQHVKGGTPKRPNRAIETYLFAMFDENKKQPEVEK 334
# F N + Y+ + + K +++++ D + Q +
# Sbjct 428 DLGEKHNDVNFGTQDHNRKYYIQRHLLSMHDAICKDKVNVTGYFVWSLMDNFEWQDGYKA 487
# Query 335 HFGLFF 340
# FGL++
# Sbjct 488 RFGLYY 493


with open ('resultado11.txt', 'r') as arq:
    for linha in arq:
        linha=linha.strip()
        if linha.startswith("Identities"):
            infos = linha.split(', ')

            results = list()

            for iter in infos:
                elements = iter.split(' ')
                id = elements[0]
                percentage = elements[-1]

                new_tuple = tuple((id, percentage))

                results.append(new_tuple)

            break

results = results + results

print(results)

# conhecendo a posição

print(results[0])
print("========")

# posição que a tupla está
for iter in range(len(results)):
    tupla = results[iter]
    if tupla[0] == "Identities":
        print(iter)
        print(tupla)

print("========")

# tupla cujo 1o elemento == "Identities"
for tupla in results:
    if tupla[0] == "Identities":
        print(tupla)


print("========")

for iter in range(len(results)):
    if results[iter][0] == "Identities":
        continue
    print(iter, results[iter])
    




# 12. Faça um programa que leia um arquivo FASTA contendo múltiplos
# identificadores e sequências. Para cada identificador e sequência o programa deve
# criar um arquivo de saída contendo o identificar e sua respectiva sequência. O nome
# dos arquivos de saída devem ser iguais aos seus respectivos identificadores,
# seguido de “.fasta”.
# Exemplo entrada:
# >Rosalind_10
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGC
# GTGTTTCAAAGTTTGCGCCTAG
# >Rosalind_12
# ATCGGTCGAA
# >Rosalind_15
# ATCGGTCGAGCGTGT
# Arquivos de saída:
# Rosalind_10.fasta
# Rosalind_12.fasta
# Rosalind_15.fasta


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


# 13. Faça um programa que leia um arquivo contendo várias strings n, onde n são os
# caminhos dos arquivos de entrada FASTA. O programa deve ler o conteúdo de cada
# arquivo de entrada e transformar em um único arquivo FASTA (nomeado como
# “all.fasta”), contendo todas os identificadores e sequências de cada arquivo de
# entrada lido.
# Exemplo entrada:
# Rosalind_10.fasta
# Rosalind_12.fasta
# Rosalind_15.fasta
# Arquivo “all.fasta” de saída:
# >Rosalind_10
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGC
# GTGTTTCAAAGTTTGCGCCTAG
# >Rosalind_12
# ATCGGTCGAA
# >Rosalind_15
# ATCGGTCGAGCGTGT

nome = []
seq = []
concatenado = []

with open ('Rosalind_10.txt', 'r') as arq1, open  ('Rosalind_12.txt', 'r') as arq2, open ('Rosalind_15.txt', 'r') as arq3:
    for linha in arq1:
        linha = linha.strip()
        if linha.startswith(">"): nome.append(linha)
        else: seq.append(linha)
    
    for linha in arq2:
        linha = linha.strip()
        if linha.startswith(">"): nome.append(linha)
        else: seq.append(linha)

    for linha in arq3:
        linha = linha.strip()
        if linha.startswith(">"): nome.append(linha)
        else: seq.append(linha)


print(nome, seq)


for i in range(len(nome)):
    concatenado.append(tuple((nome[i], seq[i])))

with open ('all.fasta', 'w') as arq_all:
    for i in concatenado:
        arq_all.write(str(i) + '\n')
        
        

with open('all.fasta', 'w') as arq_all:
    for i in concatenado:
        identificador = i[0].replace("(", "").replace(")", "").replace("'", "")
        sequencia = i[1].replace("(", "").replace(")", "").replace("'", "")
        
        arq_all.write(identificador + '\n')
        arq_all.write(sequencia + '\n')

with open ('all.fasta', 'r') as arq_all:
    print(arq_all.read())
'''
# 14. Faça um programa que leia um arquivo contendo várias linhas onde cada linha
# possui uma string a separada por espaço de uma string c, onde a é um aminoácido
# em um determinado formato (“nome”,”sigla”,”letra”) e c é o formato a ser
# convertido de a. O programa deve retornar todas as conversões de a para o formato
# c. Segue Tabela de aminoácidos.
# Exemplo entrada:
# ALA nome
# V sigla
# Tirosina letra
# Saída:
# Alanina
# Val
# Y

nome = []
sigla = []
letra = []

output = []


with open ('pc_15.txt', 'r') as arq:
    for lines in arq:
        lines = lines.split()
        if 'nome' in lines:
            nome.append(lines[0])
        if 'sigla' in lines:
            sigla.append(lines[0])
        if 'letra' in lines:
            letra.append(lines[0])    
            
# print(nome, sigla, letra)

# primeiro termo key, segundo value
amino = {
    'A': ('Alanina', 'ALA'),
    'B': ('Asparagina ou Aspartato', 'ASX'),
    'C': ('Cisteína', 'CYS'),
    'D': ('Aspartato (Ácido aspartico)', 'ASP'),
    'E': ('Glutamato (Ácido glutâmico)', 'GLU'),
    'F': ('Fenilalanina', 'PHE'),
    'G': ('Glicina', 'GLY'),
    'H': ('Histidina', 'HIS'),
    'I': ('Isoleucina', 'ILE'),
    'K': ('Lisina', 'LYS'),
    'L': ('Leucina', 'LEU'),
    'M': ('Metionina', 'MET'),
    'N': ('Asparagina', 'ASN'),
    'P': ('Prolina', 'PRO'),
    'Q': ('Glutamina (Glutamida)', 'GLN'),
    'R': ('Arginina', 'ARG'),
    'S': ('Serina', 'SER'),
    'T': ('Treonina', 'THR'),
    'V': ('Valina', 'VAL'),
    'W': ('Triptofano (Triptofana)', 'TRP'),
    'Y': ('Tirosina', 'TYR'),
    'Z': ('Glutamina ou Glutamato', 'GLX')
}

for i in nome:
    for key, value in amino.items():
        if i in value:
            output.append(value[0])
            

for i in sigla:
    for key, value in amino.items():
        if i in key:
            output.append(value[-1])
            


for i in letra:
    for key, value in amino.items():
        if i in value:
            output.append(key)
            
for i in output:
    print(i)

# 15. Estruturas de proteínas podem ser representadas por arquivos. Esse arquivos
# recebem o formato PDB, provindo de Protein Data Bank. Dentro de arquivos PDBs
# podemos encontrar muitas informações sobre uma proteína, como método
# experimental utilizado, atributos do experimento, posições espaciais do átomos dos
# aminoácidos e solvente presente, etc. Apesar do Protein Data Bank prover o
# formato FASTA (estrutura primária) de uma proteína em sua base de dados, nem
# sempre elas são idênticas a sequência encontrada no arquivo PDB e por isso para
# garantir essa exatidão é necessário realizar a conversão de um arquivo de
# sequências de aminoácidos (FASTA) a partir do arquivo de estrutura (PDB) de uma
# proteína. Sendo assim, faça um programa que leia um arquivo PDB. O programa
# deve converter o arquivo PDB para o formato FASTA, onde cada identificar do
# arquivo FASTA contenha a sequência de aminoácidos de cada cadeia polipeptídica
# do arquivo PDB.
# Exemplo entrada:
# 1A1M.pdb
# Saída:
# >1A1M_A
# GSHSMRYFYTAMSRPGRGEPRFIAVGYVDDTQFVRFDSDAASPRTEPRPPWIEQEGPEYWDRNTQIFKTNTQTYRENL
# RIALRYYNQSEAGSHIIQRMYGCDLGPDGRLLRGHDQSAYDGKDYIALNEDLSSWTAADTAAQITQRKWEAARVAEQL
# RAYLEGLCVEWLRRYLENGKETLQRADPPKTHVTHHPVSDHEATLRCWALGFYPAEITLTWQRDGEDQTQDTELVETR
# PAGDRTFQKWAAVVVPSGEEQRYTCHVQHEGLPKPLTLRWEPHH
# >1A1M_B
# IQRTPKIQVYSRHPAENGKSNFLNCYVSGFHPSDIEVDLLKNGERIEKVEHSDLSFSKDWSFYLLYYTEFTPTEKDEY
# ACRVNHVTLSQPKIVKWDRDM
# >1A1M_C
# TPYDINQML
