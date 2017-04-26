from pyspark.sql.types import *

schema_signals = StructType([
    StructField("gsm", StringType(), True),
    StructField("hgnc", StringType(), True),
    StructField("expr", FloatType(), True),
    StructField("rk", FloatType(), True),
])