import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pandas as pd

args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


tb_diretores = 's3://data-lake-de-wesley/Trusted/JSON/2023/05/30/part-00000-deb8fe53-1ec1-41ae-9ad0-b263710b8d99-c000.snappy.parquet'
tb_movies = 's3://data-lake-de-wesley/Trusted/Local/Parquet/Movies/part-00000-0d0be8be-cc83-47ee-abd8-9eb92c80c4ce-c000.snappy.parquet'
tb_imdb = 's3://data-lake-de-wesley/Trusted/JSON/2023/05/30/part-00000-1680cf93-9263-41b7-bf9e-441ee7b20bf5-c000.snappy.parquet'

df_dir = spark.read.option('header', 'true').parquet(tb_diretores)
df_dir = df_dir.coalesce(1)
df_dir= df_dir.withColumnRenamed("idfilme", "id")

df_mov = spark.read.option('header', 'true').parquet(tb_movies)
df_mov = df_mov.coalesce(1)
df_mov= df_mov.withColumnRenamed("id", "imdb")
df_mov = df_mov.select("imdb", "tempoMinutos", "notaMedia")

df_imd = spark.read.option('header', 'true').parquet(tb_imdb)
df_imd = df_imd.coalesce(1)



tb_dir_imdb = df_dir.join(df_imd, df_dir.id == df_imd.idfilme)
tb_geral = tb_dir_imdb.join(df_mov, tb_dir_imdb.imdb_id == df_mov.imdb)

fato_notas = tb_geral.select("imdb", "Diretor", "notaMedia")
fato_notas.write.saveAsTable(name="fato_notas",mode="overwrite",path='s3://data-lake-de-wesley/Refined/FatoNotasAnalise/',format="parquet")

dim_diretor = tb_geral.select("Diretor", "idfilme", "imdb")
dim_diretor.write.saveAsTable(name="dim_diretor",mode="overwrite",path='s3://data-lake-de-wesley/Refined/DimDirAnalise/',format="parquet")

dim_tempo = tb_geral.select("imdb", "idfilme", "tempoMinutos" )
dim_tempo.write.saveAsTable(name="dim_tempo",mode="overwrite",path='s3://data-lake-de-wesley/Refined/DimTemAnalise/',format="parquet")

job.commit()