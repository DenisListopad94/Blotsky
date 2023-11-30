import json
from datetime import datetime, timedelta

items_store = [
    {
        "item_1": "pen",
        "date_receive": "2023-08-20",
        "price": 250000,
        "amount": 150
    },
    {
        "item_2": "iphone",
        "date_receive": "2023-11-29",
        "price": 1000000,
        "amount": 5000
    },
    {
        "item_3": "ipad",
        "date_receive": "2023-10-29",
        "price": 1000001,
        "amount": 4000
    },
    {
        "item_4": "macbook",
        "date_receive": "2023-11-30",
        "price": 999999,
        "amount": 100
    }
]

with open("Files/items.json", "w") as js:
    json.dump(items_store, js)


def filter_products(items_store, filt_price, days_ago):
    filtered_products = []
    current_date = datetime.now()

    for items in items_store:
        date_receive = datetime.strptime(items.get("date_receive"), "%Y-%m-%d")
        price = items.get("price")

        if current_date - timedelta(days=days_ago) >= date_receive and filt_price <= price:
            filtered_products.append(items)

    return filtered_products


filt_price = 100000
days_ago = 30
filtered_products = filter_products(items_store, filt_price, days_ago)

print(f"список товаров, хранящихся больше {days_ago} дней и стоимость которых превышает {filt_price} р.:")
for items in filtered_products:
    print(items)
