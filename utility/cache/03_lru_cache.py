"""
Least Recently Used(LRU)

Least Frequently Used(LFU)
"""

from functools import lru_cache

def fetch_user(user_id):
    print(f"DB에서 아이디가 {user_id}인 사용자 정보를 읽어오고 있습니다...")
    return {
        "userId": user_id,
        "email": f"{user_id}@test.com",
        "password": "test1234"
    }

@lru_cache
def get_user(user_id):
    return fetch_user(user_id)

if __name__ == "__main__":
    from random import choice

    for i in range(10):
        get_user(user_id = choice(["A01", "B02", "C03"]))
    print(get_user.cache_info())