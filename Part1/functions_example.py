import decimal

vat = 0.25
products = [
    {'name': 'klet', 'price': 100},
    {'name': 'klut', 'price': 125.5},
    {'name': 'klat', 'price': 150}
]


def calc_price_incl_vat(price, vat):
    price_sum = price+(price*vat)
    return float(price_sum)

for product in products:
    priceInclVat = decimal.Decimal(calc_price_incl_vat(product['price'], vat)).normalize()
    priceExclVat = decimal.Decimal(float(product['price']))
    print("Produkt: {product}\nPris inkl. moms {priceInclVat}kr\nPris exkl. moms {priceExclVat}kr\n\n".format(product=product['name'], priceInclVat=priceInclVat, priceExclVat=priceExclVat))