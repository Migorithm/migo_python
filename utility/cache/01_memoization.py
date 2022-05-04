cache={}

def get_user(user_id):
    if user_id not in cache : 
        print(f"Cache miss! {user_id}")
        cache[user_id] = fetch_user(user_id)
    

def fetch_user(user_id):
    print(f"Fetching user with the id '{user_id}' from DB...")
    return {
        "userId": user_id,
        "email": f"{user_id}@test.com",
        "password": "test1234"
    }


if __name__ == "__main__":
    from random import choice

    for i in range(10):
        get_user(user_id = choice(["A01", "B02", "C03"]))
    