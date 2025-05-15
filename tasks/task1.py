from pydantic import BaseModel


user_data = {"id": 1, "name": "Иван", "email": "ivan@example.com"}


class User(BaseModel):
    id: int
    name: str
    email: str


user = User(**user_data)
data_json = user.model_dump_json()
print(data_json)
