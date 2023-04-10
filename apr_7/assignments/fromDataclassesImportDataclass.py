from dataclasses import dataclass
from typing import List

@dataclass
class User:
    sub: bool
    
def notify(user: User) -> None:
    pass

# Filter users with subscription.
def find_subscribers(users: List[User]) -> List[User]:
    return[user for user in users if user.sub]

# notify users.
def notify_users(users: List[User]) -> None:
    for user in find_subscribers(users):
        notify(user)



# from typing import List
# import pandas as pd
# class User:
#     sub: bool
# def notify(user: User) -> None:
#     pass
# def notify_users(x: List[User]) -> None:
#   #Filter users with subscription and notify them.
#   for u in x:
#      if u.sub:
#       # u.notify()
#        notify(u)