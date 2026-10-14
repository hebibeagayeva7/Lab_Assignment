from functools import reduce

#data
shopping_cart = [
    {"product": "Kompüter", "price": 1200, "quantity": 1},
    {"product": "Telefon", "price": 800, "quantity": 1},
    {"product": "Qulaqlıq", "price": 50, "quantity": 2},
    {"product": "Siçan (Mouse)", "price": 30, "quantity": 3},
    {"product": "Çanta", "price": 70, "quantity": 1},
    {"product": "Fləşkart", "price": 20, "quantity": 2}
]




#umumi qiymet
item_totals = list(map(lambda item: item["price"] * item["quantity"], shopping_cart))
    print(f"Her mehsulun cemleri : {item_totals})

#umumi sebet qiymeti
cart_total = reduce (lambda x, y: x+y, item_totals)
    print(f"sebetin umumi ilkin qiymeti: {cart_total}AZN")

#50den baha olanlar
expensive_items = list(filter(lambda item: item["price"] > 50, shopping_cart))

print("qiymeti 50den baha olan mehsullar")

for exp in expensive_items:
          print(f"- {exp['product']}: {exp['price']} AZN")

#endirim sertleri
if cart_total > 500:
    discount = 0.20  # 20% endirim
elif cart_total > 300:
    discount = 0.10  # 10% endirim
elif cart_total > 100:
    discount = 0.05  # 5% endirim
else:
    discount = 0.0   # endirim yoxd


#yekun price
final_price = cart_total - (cart_total*discount)

print(f"yekun qiymet (endirimle): {final_price} AZN")
