"""
Instead of implementing your own memoization, you can use @functool.cache for better readability.
The argument passed in will be key and its result will be value so the next time the argument is passed,
it will return the stored value. 

It should be noted however, as @cache was introduced since 3.9, it's relatively new. 
"""

from functools import cache

def fetch_user(user_id):
    print(f"User with the id '{user_id} is being fetched from DB...")
    return {
        "userId": user_id,
        "email" : f"{user_id}@test.com",
        "password" : "test1234"
    }

@cache
def get_user(user_id):
    return fetch_user(user_id)

if __name__ == "__main__":
    from random import choice

    for i in range(10):
        a = get_user(user_id = choice(["A01", "B02", "C03"])) #it gets to DB only 3times 
        print(a) 