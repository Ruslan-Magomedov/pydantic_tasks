from pydantic import BaseModel


user_data = {"id": 1, "name": "Иван", "email": "ivan@example.com", "age": 30}
user_data2 = {"id": 2, "name": "Петр", "email": "petr@example.com"}


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None


user1 = User(**user_data)
user2 = User(**user_data2)

data_json1 = user1.model_dump_json()
data_json2 = user2.model_dump_json()

print(data_json1)
print(data_json2)
