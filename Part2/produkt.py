class Product:

    def __init__(self, name, price, vat):
        self.name = name
        self.price = price
        self.vat = vat

    description = "Not set"
    weight = "Not set"
    vendor = "Not set"

    def price_incl_vat(self):
        return (self.price*self.vat)+self.price

    def product_summary(self):

        product = {
            'name': self.name,
            'price': self.price,
            'priceInclVat': self.price_incl_vat(),
            'description': self.description,
            'weight': self.weight,
            'vendor': self.vendor
        }

        return product


class SpecialProduct(Product):

    def calc_price_by_length(self, length):

        price = {
            'price': self.price*length,
            'priceInclVat': self.price_incl_vat()*length
        }

        return price
