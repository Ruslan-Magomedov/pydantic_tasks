from pydantic import BaseModel


user_data = [
    {"id": 1, "name": "Иван", "email": "ivan@example.com"},
    {"id": 2, "name": "Петр", "email": "petr@example.com"}
]


class User(BaseModel):
    id: int
    name: str
    email: str

users: list[User] = [User(**user) for user in user_data]

print(users)
