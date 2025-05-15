from pydantic import BaseModel


order_data = {
        "items": [
        {"name": "Яблоко", "price": 1.5},
        {"name": "Банан", "price": 2.0}
        ]
    }


class Products(BaseModel):
    name: str
    price: float


class Order(BaseModel):
    items: list[Products]


user = Order(**order_data)
data_json = user.model_dump_json()

print(data_json)
