from Part2.produkt import Product, SpecialProduct


product1 = Product('Produkt 1', 100, 0.25)
product1.description = "En fin produkt"

product2 = Product('Produkt 2', 500, 0.25)

priceInclVat1 = product1.price_incl_vat()
priceInclVat2 = product2.price_incl_vat()

print("{priceInclVat}kr, {descr}".format(priceInclVat=priceInclVat1, descr=product1.description))
print("{priceInclVat}kr".format(priceInclVat=priceInclVat2))


product3 = SpecialProduct('Produkt 3', 2, 0.25)

priceInclVat3 = product3.calc_price_by_length(10)

print(priceInclVat3['priceInclVat'])


