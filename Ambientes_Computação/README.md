# Documentação do pipeline de ancestralidade

## Descrição 

Este pipeline realiza o controle de qualidade em dados de genótipos utilizando o software *plink* e após isso realiza a análise de ancestralidade utilizando o software *admixture*, gerando junto um gráfico de proporção de ancestralidade por indivíduo.

## Requisitos

- Python3:
      - pandas
      - numpy
      - matplotlib
- Plink 
- Admixture

Sendo necessário a instalação da biblioteca *python panda,  numpy, matplotlib* e os software *plink* e *admixture*.

## Uso

O pipeline pode ser executado a partir da linha de comando com seguintes argumentos:

*“--path”*: Caminho para o diretório contendo os arquivos .bed de entrada. 
*“--EHW”*: Valor de p para o teste de Equilíbrio de Hardy-Weinberg (sendo opcional).
*“--MAF”*: Frequência do menor alelo (sendo opcional).
*“--ADX”*: Número de clusters para análise de ancestralidade com admixture (sendo opcional).

## Estrutura do Pipeline 

### Importações:
Para conseguir realizar o pipeline é necessários importar as seguintes bibliotecas:
- *os *
- *glob*
- *argparse*
- *pandas*
- *numpy*
- *matplotlob.pyplot*


### Funções:
O pipeline utiliza das seguintes funções para realizar seus objetivos.

- ***main()***:

Essa função é responsável por definir e analisar os argumentos da linha de comando e verificar a existência de diretórios de saída e caso eles não existam criar esses diretórios. Essa função chama a função `caminho_para_chamar_arquivo`.


- ***caminho_para_chamar_arquivos(args)***:

Essa função encontra os arquivos `.bed` dentro da pasta e realiza a chamada da função `Controle_de_Qualidade`. 


- ***Controle_de_Qualidade(args, file)***:

Essa função executa o comando `plink` para realizar o controle de qualidade dos dados. Nessa função temos a opção de excluir alelos com a menor frequência, calcular o equilíbrio de Hardy-Weinberg e excluir os missing data. E essa termina chamando a função `Admixture`,para realizar a análise de ancestralidade.


- ***Admixture(args, name, file)***:

Essa função executa o comando do `admixture` para análise da ancestralidade, os arquivos de output são movidos para um outro diretório chamado `Output_admixture` e para terminar essa função chama a função `Plot` para gerar gráficos.


- ***Plot(file_2)***:

Essa função é responsável por criar um gráfico de barra empilhada mostrando as proporções de ancestralidade para cada indivíduo a partir do arquivo `.Q` gerado pelo admixture.



## Complexidade do pipeline

A complexidade desse pipeline além das funções usadas, também depende dos softwares externos usados como *plink* e *admixture* e para uma análise específica de complexidade temporal e espacial para os comandos usando os dois software não podem ser determinados diretamente pelo script do pipeline. Outro fator que vai influenciar nessa complexidade é o tamanho dos arquivos usados para input e os gerados de output.

- Função *main*:

Espacial: Irá depender dos arquivos que serão processados.
Temporal: Considera a  complexidade da função `caminho_para_chamar_arquivos`

- Função *caminho_para_chamar_arquivos*:

Espacial: Irá depender dos arquivos processados. 
Temporal: Considera a  complexidade da função `Controle_de_Qualidade`.

- Função *Controle_de_Qualidade*:
 
Espacial: Considera a complexidade do software *plink* e dos arquivos gerados por ele.
Temporal: Possui uma complexidade de *O(n x complexidade de os.system())*. A complexidade de `os.system()` depende do software *plink*.

 
- Função *Admixture*:

Espacial: Considera a complexidade do software *admixture* e os arquivos gerados nele.
Temporal: Possui uma complexidade de *O(n x complexidade de os.system())*. A complexidade de `os.system()` depende do software *admixture*. 

- Função *Plot*:

Espacial: Possui uma complexidade de *O(m x n)*. Sendo que *m* é número de colunas e *n* o número de linhas 
Temporal: Possui uma  complexidade de *O(n + m  x n)*. Sendo que *m* é número de colunas e *n* o número de linhas 
