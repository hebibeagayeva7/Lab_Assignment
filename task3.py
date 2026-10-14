def make_discount (percent):
    def apply_discount(price):
        return price - (price * (precent/100)) #qiymetden faizi cxrg
    return apply_discount

discount_5 = make_discount(5)
discount_10 = make_discount(10)
discount_20 = make_discount(20)

#sinaq ucun qiymetler (initial qiymetleri)
prices = [50,100,200,500,1200]
print(f"ilkin qiymetler: {prices}")

#endirimleri tetbiq edirem
prices_with_5_precent = list(map(discount_5, prices))
prices_with_10_precent = list(map(discount_10, prices))
prices_with_20_precent = list(map(discount_20, prices))

#results
print(f"5% endirimli qiymetler: {prices_with_5_precents}")
print(f"10% endirimli qiymətlər: {prices_with_10_percent}")
print(f"20% endirimli qiymətlər: {prices_with_20_percent}")
