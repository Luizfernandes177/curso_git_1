from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
import pyspark.sql.functions as randomica



spark = SparkSession \
        .builder \
        .master("local[*]")\
        .appName("Exercicio Intro") \
        .getOrCreate()

df_nomes = spark.read.csv('/Users/Luiz Fernandes/Documents/github/Compass-Uol-Udemy/Sprint8/tarefa3/nomes_aleatorios.txt')
escolaridade = ['Fundamental', 'Medio' , 'Superior']
df_nomes = df_nomes.withColumnRenamed('_c0','Nomes')
df_nomes = df_nomes.withColumn("Escolaridade", randomica.lit(escolaridade).getItem((randomica.rand() * 3).cast("int")))

paises = ['Brasil', 'Argentina', 'Uruguai', 'Chile', 'Bolivia', 'Peru', 'Equador', 'Venezuela', 'Colombia', 'Guiana', 'Guiana Francesa', 'Suriname', 'Paraguai']
df_nomes = df_nomes.withColumn("Pais", randomica.lit(paises).getItem((randomica.rand() * 13).cast("int")))

ano = list(range(1945,2011))
df_nomes = df_nomes.withColumn("AnoNascimento", randomica.lit(ano).getItem((randomica.rand() * len(ano)).cast("int")))

#df_select = df_nomes.filter(df_nomes.AnoNascimento>=2000)

#df_select.createOrReplaceTempView ("pessoas")
#spark.sql("select * from pessoas").show(10)

#Millennials = df_nomes.filter((df_nomes.AnoNascimento>=1980)&(df_nomes.AnoNascimento<=1994))
#Quantidade = Millennials.count()
#print(f'Existem {Quantidade} pessoas nascidas nesse período!')

#Millennials.createOrReplaceTempView ("Millennials")
#spark.sql("select * from Millennials").show(10)


df_nomes = df_nomes.withColumn('Geracao', randomica.when((randomica.col('AnoNascimento') >= 1944) & (randomica.col('AnoNascimento') <= 1964), 'Baby Boomers')
                                                .when((randomica.col('AnoNascimento') >= 1965) & (randomica.col('AnoNascimento') <= 1979), 'Geração X')
                                                .when((randomica.col('AnoNascimento') >= 1980) & (randomica.col('AnoNascimento') <= 1994), 'Millennials')
                                                .when((randomica.col('AnoNascimento') >= 1995) & (randomica.col('AnoNascimento') <= 2015), 'Geração Z')
                                                .otherwise('Outra'))
df_nomes.createOrReplaceTempView("FINAL")
x_generation = spark.sql("SELECT Pais, Geracao, COUNT(*) AS Quantidade FROM FINAL GROUP BY Pais, Geracao ORDER BY Pais, Geracao")
x_generation.show(52)




#df_nomes.printSchema()

