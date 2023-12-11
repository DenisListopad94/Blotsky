import json
from datetime import datetime, timedelta

with open("Files/items.json", "r") as js:
    items2 = json.load(js)


def filter_products(items2, filt_price, days_ago):
    filtered_products = []
    current_date = datetime.now()

    for items in items2:
        date_receive = datetime.strptime(items.get("date_receive"), "%Y-%m-%d")
        price = items.get("price")

        if current_date - timedelta(days=days_ago) >= date_receive and filt_price <= price:
            filtered_products.append(items)

    return filtered_products


print(js)
js.close()

filt_price = 100000
days_ago = 30
filtered_products = filter_products(items2, filt_price, days_ago)

print(f"список товаров, хранящихся больше {days_ago} дней и стоимость которых превышает {filt_price} р.:")
for items in filtered_products:
    print(items)
