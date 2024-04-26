import time
inicio = time.time()
# seu código deve iniciar aqui
from Bio.PDB import *
from Bio.SeqUtils import *

def pdb_to_fasta(pdb_file):
    '''
    *   Lê um arquivo pdb 
    *   retorna a sequência em fasta 
    *   usando Biopython 
    '''
    parser = PDBParser()
    structure = parser.get_structure('structure', pdb_file)
    sequence = ''
    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.get_id()[0] == ' ':
                    sequence += seq1(residue.get_resname())
    return sequence

def main():
    ''' Função principal '''
    pdb_file = "3RGK.pdb"  # arquivo de entrada
    try:
        fasta_sequence = pdb_to_fasta(pdb_file)
        print(">Mioglobina humana | PDB ID: 3RGK")
        print(fasta_sequence)
    except Exception as e:
        print("Ocorreu um erro:", e)

# chamada a função principal
if __name__ == "__main__":
    main()

# seu codigo deve terminar aqui
fim = time.time()
tempo = round(fim - inicio, 3)
print(f"Tempo total de execução: {tempo}s")
'''
***************************************************************
SAÍDA ESPERADA: 
***************************************************************
>Mioglobina humana | PDB ID: 3RGK
GLSDGEWQLVLNVWGKVEADIPGHGQEVLIRLFKGHPETLEKFDRFKHLKSEDEMKASEDLKK
HGATVLTALGGILKKKGHHEAEIKPLAQSHATKHKIPVKYLEFISEAIIQVLQSKHPGDFGAD
AQGAMNKALELFRKDMASNYKEL
***************************************************************
Tempo total de execução: 0.733s
***************************************************************
'''