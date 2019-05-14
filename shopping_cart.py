#use a import statement
from products import Product
#Your program should have two separate classes:
class ShoppingCart:


#Each shopping cart has a collection of products.
    def __init__(self):
        self.products =[]
#functionality:
#add an product to the cart
    def add_product(self, product):
        self.products.append(product)

#remove an product from the cart
    def remove_product(self, product):
        self.products.remove(product)
#add up the total cost of all products in the cart before tax
    def total_before_tax(self):
        total = 0
        for product in self.products:
            total += product.base_price
        return total
#add up the total cost of all products in the cart after tax
    def total_after_tax(self):
        total = 0
        for product in self.products:
            total = total + (product.base_price * (1 + product.tax_rate / 100))
        return total

#Add the ability to find the most expensive product in a cart.
