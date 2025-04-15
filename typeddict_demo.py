from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


new_person: Person = {"name": "ankit", "age": 26}

print(new_person)
