import pytest
from pymongo import MongoClient


@pytest.fixture
def mongodb_client():
    # MongoDB 연결 설정
    mongodb_uri = "답안을 채워주세요"
    client = MongoClient(mongodb_uri)
    yield client
    client.close()


def test_avg_rating_for_movie(mongodb_client):
    # movies 데이터베이스와 avg_ratings 컬렉션 선택
    db = mongodb_client["movies"]
    collection = db["avg_movie_ratings"]

    # 특정 movieId에 대한 avg_rating 검증
    movie_id = "106022"
    answer = 4

    # 데이터 조회
    result = collection.find_one({"movieId": movie_id})
    assert result is not None, f"movieId {movie_id} 데이터가 없습니다"
    assert result["avg_rating"] == answer, (
        f"avg_rating: 답안 ({answer}) != 제출된 데이터 ({result['avg_rating']})"
    )