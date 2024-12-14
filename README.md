# 개요

영화 평점 데이터를 활용해 ETL(Extract, Transform, Load) 과정을 구현하고, 평균 평점 데이터를 생성하여 MySQL과 MongoDB 간의 데이터 파이프라인을 개발하는 실무형 과제 테스트입니다.

주어진 요구사항에 따라 Docker 기반 환경에서 MySQL, MongoDB, 그리고 PySpark를 활용한 데이터 파이프라인을 개발해야 합니다.

# 시스템 요구사항

1. mysql 은 8.0 으로 구성
2. mongodb 는 percona server for mongodb 6.0.6 으로 구성
3. spark 는 3.2.3 으로 구성

# 문제

1. 수정해야 하는 코드들은 다음과 같습니다
    * "답안을 채워주세요" 로 되어 있는 부분들과 pass 로 비어있는 함수들을 작성해주세요
    * 수정 및 완성시켜야 하는 코드들은 다음과 같습니다
        * docker-compose.yml
        * app/main.py
        * app/tests/test\_mongodb.py
        * app/tests/test\_mysql.py
2. docker-compose.yml 를 수정하여 시스템 요구사항에 맞는 데이터베이스와 스파크 클러스터를 구성합니다.
3. app/main.py 에 데이터 파이프라인들을 개발합니다
    1. data 폴더에 있는 영화 평점 데이터를 pyspark 를 통해 mysql 에 넣습니다
        * app/main.py 내 load\_data\_to\_mysql 함수 개발
        * mysql 데이터베이스명: movies
        * mysql 테이블명: movie\_ratings
        * 권장 스키마는 테이블 스키마 섹션을 참고해주세요
    2. mysql 에 적재된 데이터를 pyspark 를 통해 영화별로 평균 평점을 집계하여 mongodb 에 넣습니다
        * app/main.py 내 calculate\_and\_save\_to\_mongodb 함수 개발
        * mongodb 데이터베이스명: movies
        * mongodb 컬렉션명: avg\_movie\_ratings
    3. mongodb 에 적재된 영화별 평균 평점 데이터를 pyspark를 통해 mysql 에 넣습니다
        * app/main.py 내 save\_avg\_ratings\_to\_mysql 함수 개발
        * mysql 데이터베이스명: movies
        * mysql 테이블명: avg\_movie\_ratings
        * 권장 스키마는 테이블 스키마 섹션을 참고해주세요

## 테이블 스키마

### mysql

#### movies.movie\_ratings

| 컬럼명 | 데이터 타입 | 스파크 데이터타입 |
| --- | ------ | --------- |
| userId | text | StringType |
| movieId | text | StringType |
| rating | float | FloatType |
| timestamp | bigint | LongType |

#### movies.avg\_movie\_ratings

| 컬럼명 | 데이터 타입 | 스파크 데이터타입 |
| --- | ------ | --------- |
| \_id | text | StringType |
| avg\_rating | float | FloatType |
| movieId | text | StringType |

# 평가 방법

1. 디렉토리 최상단에서 mysql, mongodb, spark 도커 컨테이너가 실행되어야 합니다

    ```bash
    docker-compose up -d
    ```
2. spark-master 컨테이너로 진입합니다

    ```bash
    docker exec -it spark-master /bin/bash
    ```
3. 실행에 필요한 모듈을 설치합니다

    ```bash
    pip install -r /app/requirements.txt
    ```
4. pyspark 앱을 로컬 모드로 실행합니다

    ```bash
    python /app/main.py
    ```
5. 개발 완료 후, 기능들이 정상적으로 수행되는지 검증합니다
    * 모든 테스트 케이스들 (3개) 에 대해서 통과해야 합니다

    ```bash
    python3 -m pytest /app/tests
    
    hello@093f0f85b79d:/opt/bitnami/spark$ python3 -m pytest /app/tests
    ============================================== test session starts ==============================================
    platform linux -- Python 3.9.16, pytest-8.3.4, pluggy-1.5.0
    rootdir: /app/tests
    collected 3 items
    
    ../../../app/tests/test_mongodb_answer.py .                                                               [ 33%] 
    ../../../app/tests/test_mysql_answer.py ..                                                                [100%]
    
    =============================================== 3 passed in 0.21s ===============================================
    ```

# DB 관련 cheat sheet

## MySQL

* 도커 내 mysql shell 접근하기

    ```
    docker exec -it mysql mysql -uyour_user -pyour_password
    ```
* 데이터베이스 생성하기

    ```
    create database your_database;
    ```
* 데이터베이스 조회

    ```
    show databases;
    ```
* 사용할 데이터베이스 활성화

    ```
    use your_database;
    ```
* 테이블 조회

    ```
    show tables;
    ```
* 테이블 스키마 조회

    ```
    describe your_table;
    ```
* 데이터베이스 제거하기

    ```
    drop database your_database;
    ```
* 테이블 제거하기

    ```
    truncate your_table;
    ```

## MongoDB

* 도커 내 mongodb shell (mongosh) 접근하기

    ```
    docker exec -it mongodb mongosh
    ```
* 데이터베이스 및 컬렉션 생성

    ```
    use your_database;
    db.createCollection("your_collection");
    ```
* 데이터베이스 및 컬렉션 조회

    ```
    show dbs;
    show collections;
    ```
* 컬렉션 내 데이터 조회

    ```
    db.your_collection.find().pretty();
    ```
* 데이터베이스 제거하기

    ```
    use your_database;
    db.dropDatabase();
    ```
* 컬렉션 제거하기

    ```
     db.your_collection.drop();
    ```