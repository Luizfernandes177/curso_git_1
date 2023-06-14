# Relatório da Sprint 8 #

## WESLEY LUIZ FERNANDES ##

## Objetivo do projeto ##

Tema:

Somente pesquisa sobre filmes de animação.

Objetivo:

Veirificar se as maiores notas são por filmes com diretores com maior quantidade de produção cinematografica ou duração dos filmes.

Método:

Agrupar diretor, fazer a contagem de produções e a média da nota de todas as produções. 
Agrupar por faixa de notas e verificar a duração média em cada faixa.


Discussão:

Analisar se existe alguma correlação entre as faixas de notas dos filmes e a duração. Além de analisar se os diretores que mais produzem são os que tem as melhores notas.

Intuito:

Avaliar se é valido muito investimento ou não nos diretores, o tempo ideal para o maior sucesso e se contratar diretores experientes é sempre válido.


**Tarefa 1** 

Com o objetivo de puxar os dados de uma API, foram feitos os seguintes passos para tal:

- Fazer o import da biblioteca 'requests'
- Criação da conta na API
- Inserção da chave de acesso e da url com a chave de acesso no código local
- Usar o get para puxar os dados da API
- Transformar os dados em JSON
- Criação de uma lista 'directors' onde os dados serão armazenados
- Verificar as chaves dos dados e verificar quais serão usadas (nesse código foram usadas as chaves 'total_pages' e 'results')
- Utilização de um loop para percorrer página por página por meio da URL dos dados com os filtros inseridos pelo objetivo
- Em cada página ele irá salvar os ID dos filmes no novo 'data'
- Dentro desse loop anterior, utilizar um novo loop para acessar a chave 'results' dentro do novo 'data' que contem os dados detalhados do filme, inclusive os diretores na chave 'crew' dentro do 'results'
- Dentro desse loop anterior, verificar cada filme pelo ID e acessar a chave 'crew' para verificar a nova chave 'job' dentro do 'crew'
- Utilizar uma condição de igualdade de valores, se o valor do 'job' for igual a 'Director' então o loop continua a percorrer
- Utilizar um enumerate for items para adicionar a lista 'directors' o 'name' (dado incluso dentro da chave 'crew' que está sendo percorrida) e o ID do filme incluso dentro da chave 'results'

**Tarefa 2** 

- Após os passos da Tarefa 1, fazer o import das bibliotecas : pandas, json, boto3, logging, botocore.exceptions, io
- Colocar todo o código dentro de uma def
- Utilizar o boto3 para fazer o acesso a permissão de acesso no s3
- Utilizar o resource para integração com objetos
- Criar uma def de tentativa de criação de bucket, caso o bucket não exista, criar um  e passar os parametros (nome, localização e privacidade)
- Para criação dos arquicos json é necessário criar um contador de 100 em 100 elementos e uma lista de quantidade blocos para colocar esses 100 elementos
- Para que o loop não seja infinito, utilizar um len para verificar o tamanho que o loop posterior irá percorrer
- Nesse loop será percorrido a lista 'directors' criada anteriormente colocando de 100 em 100 diretores em cada bloco
- Ao final de cada bloco será criado um arquivo json diretamente no S3 com o utilização da função put_object, porém os arquivos devem ser transformados em binários antes com a função BytesIO


**Tarefa 3**

- Na tarefa 3 foram revistos as formas de acesso e criação de um arquivo localmente
- Foi utilizado também a função 'choice()' para aleatorização dos dados em uma lista
- Foi criado um arquivo txt com nomes aleatórios para uso na atividade seguinte

**Tarefa 4**

- Para utilização e configuração do spark fazer o import das bibliotecas: 'pyspark.sql', 'pyspark'  e 'pyspark.sql.functions'
- Foram utilizados métodos para abertura de arquivos com o read.csv, renomeação de colunas com o withColumnRenamed, criação de novas colunas com o withColumn, colocação de dados aleátorios em cada coluna com a função 'pyspark.sql.functions' e o devido uso no spark.sql para uso dos dados temporários.


# Conclusão #

    Nessa sprint podemos verificar como fazer o acesso de uma API e o consumo desses dados. Posteoriormente como que esses dados podem alimentar o bucket e criar arquivos com eles. Por fim, o que pode ser manipulado com esses dados e como manipular para utiliza-los.
