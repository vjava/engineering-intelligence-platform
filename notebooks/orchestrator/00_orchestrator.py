
from pyspark.sql import Row

data = [
 Row(application='Payments',risk='HIGH',vulnerabilities=12),
 Row(application='Cards',risk='LOW',vulnerabilities=5),
 Row(application='Retail',risk='CRITICAL',vulnerabilities=20)
]

spark.createDataFrame(data).write.mode('overwrite').saveAsTable('eng_gold_release_health')
print('Pipeline completed')
