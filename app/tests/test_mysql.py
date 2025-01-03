import pytest
import mysql.connector


@pytest.fixture
def mysql_connection():
    # MySQL 연결 설정
    conn = mysql.connector.connect(
        host="답안을 채워주세요",  # MySQL이 실행 중인 호스트
        user="답안을 채워주세요",       # MySQL 사용자
        password="답안을 채워주세요",  # MySQL 비밀번호
        database="답안을 채워주세요"  # 사용할 데이터베이스
    )
    yield conn
    conn.close()


def test_movie_id_count(mysql_connection):
    movie_id = "106022"
    answer = 1

    cursor = mysql_connection.cursor()
    
    # movieId가 106022인 데이터의 개수를 조회하는 SQL 쿼리
    query = f"SELECT COUNT(*) FROM movie_ratings WHERE movieId = '{movie_id}'"
    cursor.execute(query)
    result = cursor.fetchone()
    
    # 결과 검증
    assert result is not None, f"movieId {movie_id} 데이터가 없습니다"
    assert result[0] == answer, f"movieId {movie_id} 데이터 개수: 답안 ({answer}) != 제출된 데이터 {result[0]}"
    

def test_avg_rating_for_movie(mysql_connection):
    movie_id = "106022"
    answer = 4

    cursor = mysql_connection.cursor()
    
    # movieId가 106022인 데이터의 개수를 조회하는 SQL 쿼리
    query = f"SELECT avg_rating FROM avg_movie_ratings WHERE movieId = '{movie_id}'"
    cursor.execute(query)
    result = cursor.fetchone()
    
    # 결과 검증
    assert result is not None, "movieId 106022 데이터가 없습니다"
    assert result[0] == answer, f"avg_rating: 답안 ({answer}) != 제출된 데이터 ({result[0]})"