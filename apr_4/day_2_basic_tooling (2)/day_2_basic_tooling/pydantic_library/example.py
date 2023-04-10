from typing import List

import pydantic


class Hobby(pydantic.BaseModel):
    name: str
    is_a_team_hobby: bool


class Person(pydantic.BaseModel):
    first_name: str
    last_name: str
    hobbies: List[Hobby]


hobby = Hobby(name='Reading', is_a_team_hobby=False)
tempDict = hobby.dict()
print(tempDict)

anotherHobby = Hobby(**tempDict)
print(anotherHobby)

