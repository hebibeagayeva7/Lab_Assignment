



shopping_cart = [
    {"product": "Komputer", "price": 1200, "quantity": 1},
    {"product": "Telefon", "price": 800, "quantity": 1},
    {"product": "Qulaqliq", "price": 50, "quantity": 2},
    {"product": "Mouse", "price": 30, "quantity": 3},
    {"product": "Canta", "price": 70, "quantity": 1},
    {"product": "Fles kart", "price": 20, "quantity": 2}
]

 cart_total= 0

 for item in shopping_cart:
     name = item["product"]
     price = item["price"]
     quantity =  item["quantity"]

     item_total = price * quantity

     cart_total = cart_total + item_total

     #side effect, her mehsulun infolari
     print( f"Mehsul: {name} / Qiymet; {price} AZN | Say: {quantity} | Cemi: {item_total} AZN")


#butun itemlerin umumi cemi
print(f"\nSebetin ilkin umumi qiymeti: {cart_total} AZN")
if cart_total > 500:
    discount = 0.20 #eger 500den coxdursa 20% endirim
    print ("endirim: 20% tetbiq olundu")
elif cart_total > 300:
    discount 0.10 #300den coxdursa 10% endirim
    print ("endirim: 10% tetbiq olundu")
elif cart_total > 100:
    discount + 0.05 #100den coxdursa 5%
    print ("endirim: 5% tetbiq olundu")
else:
    discount = 0.0 #100den azdisa


final_price = cart_total - (cart_total * discount) #yekun

print(f"orijinal qiymet: {cart_total} AZN")
print(f"yekun qiymet (endirimle) : {final_price} AZN) 



