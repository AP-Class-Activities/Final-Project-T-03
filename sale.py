'''
This is a class defining the products that have been selled by the sellers and bought by the customers.
This class has access to the product class, date class, customer class and the seller class.

Usage:
    1) Create a new sale:
       Sale(product,seller,customer,date)
    2) Print a sale information:
       print(sale)


'''
from Products import Product
from users import Customer, Seller
import jdatetime

class Sale:
    def __init__(self, product, customer, date = jdatetime.datetime.now()):
        if type(product) is Product:
            self.__product = product
        else:
            raise ValueError('Product should be a Product!')
        
        if type(customer) is Customer:
            self.__customer = customer
        else:
            raise ValueError('Customer should be a Customer!')

    # date = datetime.datetime.now()

    # setter and getter

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self,value):
        if type(value) is Product:
            self.__product = value
        else:
            raise ValueError('Product should be a Product!')     

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self,value):
        if type(value) is Customer:
            self.__customer = value
        else:
            raise ValueError('Customer should be a Customer!')


    def __str__(self):
        return '\n Product:\n' + str(self.product) + '\n Customer:\n' + str(self.customer) + '\n Date:\n' + str(self.date)

x = Product ( 123456, 'book' , 50000 , 15, ['good','nice'],[4,3,4,2])
# s = Sale(x,)