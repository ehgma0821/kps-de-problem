from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StringType, FloatType, LongType


# 1단계: MySQL에 CSV 데이터 적재
## 힌트: mysql 관련 옵션 (url, dbtable, user, password, driver=com.mysql.cj.jdbc.Driver)
def load_data_to_mysql(spark, mysql_url):
    pass


# 2단계: MySQL에 적재되어 있는 데이터를 load하여 movieId별 평균 평점을 계산한 뒤, MongoDB에 적재
## 힌트: mysql 관련 옵션 (url, dbtable, user, password, driver=com.mysql.cj.jdbc.Driver)
## 힌트: mongodb 관련 옵션 (connection.uri, database, collection)
def calculate_and_save_to_mongodb(spark, mysql_url, mongodb_uri):
    pass


# 3단계: MongoDB에 적재한 집계 (마트) 데이터를 MySQL로 ETL
## 힌트: mongodb 관련 옵션 (connection.uri, database, collection)
## 힌트: mysql 관련 옵션 (url, dbtable, user, password, driver=com.mysql.cj.jdbc.Driver)
def save_avg_ratings_to_mysql(spark, mongodb_uri, mysql_url):
    pass


if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("MovieRatingsApp") \
        .config("spark.jars", "답안을 채워주세요") \
        .getOrCreate()

    mysql_url = "답안을 채워주세요"
    mongodb_uri = "답안을 채워주세요"

    load_data_to_mysql(spark, mysql_url)
    calculate_and_save_to_mongodb(spark, mysql_url, mongodb_uri)
    save_avg_ratings_to_mysql(spark, mongodb_uri, mysql_url)