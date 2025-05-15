from pydantic import BaseModel


user_data = {
    "id": 1,
    "name": "Иван",
    "email": "ivan@example.com",
    "address": {"street": "Тверская", "city": "Москва", "zip_code": "123456"}
}


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address


user = User(**user_data)
data_json = user.model_dump_json()

print(data_json)
