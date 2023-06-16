# Relatório da Sprint 9 #

## WESLEY LUIZ FERNANDES ##

## Objetivo do projeto ##

Tema:

Somente pesquisa sobre filmes de animação.

Objetivo:

Veirificar se as maiores notas são por filmes com diretores com maior quantidade de produção cinematografica, maior orçamento ou duração dos filmes.

Método:

Agrupar diretor, fazer a contagem de produções e a média da nota de todas as produções. 
Agrupar por faixa de notas e verificar a duração média em cada faixa.


Discussão:

Analisar se existe alguma correlação entre as faixas de notas dos filmes e a duração. Além de analisar se os diretores que mais produzem são os que tem as melhores notas.

Intuito:

Avaliar se é valido muito investimento ou não nas produções, o tempo ideal para o maior sucesso e se contratar diretores experientes é sempre válido.


**Tarefa 1** 

Com o objetivo de criar e desenvolver tabelas relacionais, foram feitos os seguintes passos:

- Primeiramente foi feito a divisão das tabelas por entidade (Cliente, Carro, Vendedor e Aluguel)
- Depois foi verificado as colunas chaves (Chaves primárias e Estrangeiras) de cada entidade para criar a relação entre elas.
- Por fim, foi feito a normalização das colunas, colocando colunas com dados repetidos em novas tabelas, fazendo-se necessário então a criação de duas novas tabelas. 

**Tarefa 2** 

Com o objetivo de criar e desenvolver modelos dimensionais, foram feitos os seguintes passos:

- Criação de views com o uso das tabelas relacionais como fonte.
- Escolha de uma tabela fato que contem dados relacionados as ações que acontecem com o objeto e variaveis que sejam inteiras.
- Distribuição de chaves primarias e chaves estrangeiras para relacionar as tabelas.
- Entendimento das distribuições de forma que possam ser feitos cortes, inversão e granulamento dos dados.


**Tarefa 3**

Na atividade foi desenvolvido o modelo multidimensional para o utilização dos dados do projeto final. Foram levados em consideração para subdivisão dos dados os seguintes fatores:

- Seleção de somente os dados que serão utilizados.
- Agregação dos dados em fato e dimensões.
- Relacionamento dos dados.

**Tarefa 4**

Na última tarefa foram feitos os seguintes passos para a criação das tabelas e alimentação delas:

- Leitura dos arquivos parquet previamente criados no bucket.
- Transformação dos arquivos em DataFrames para manipulação.
- Joins entre os dataframes em um arquivo único.
- Seleção das colunas para realocação em uma nova tabela.
- Criação de um database glue e criação das novas tabelas.


# Conclusão #

    Nessa sprint podemos verificar como fazer a modelagem e o relacionamento dos dados, assim como a criação de databases e tabelas para uso na aws. Posteoriormente como que esses dados podem alimentar o bucket e criar tabelas com o uso do glue. Por fim, o que pode ser manipulado com esses dados e como manipular para utiliza-los.
