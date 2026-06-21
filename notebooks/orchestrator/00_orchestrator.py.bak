
from pyspark.sql import Row

data=[
 Row(application='Payments',team='Core',vulnerabilities=12),
 Row(application='Cards',team='Cards',vulnerabilities=5),
 Row(application='Retail',team='Retail',vulnerabilities=20)
]

spark.createDataFrame(data).write.mode('overwrite').saveAsTable('eng_gold_release_health')
print('Pipeline completed')
