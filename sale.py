'''
This is a class defining the products that have been selled by the sellers and bought by the customers.
This class has access to the product class, date class, customer class and the seller class.

Usage:
    1) Create a new sale:
       s = Sale(product,seller,customer)
    2) Print a sale information:
       print(s)


'''
from Products import Product
from users import Customer, Seller
import jdatetime

class Sale:
    def __init__(self, product, seller, customer):
        if type(product) is Product:
            self.__product = product
        else:
            raise ValueError('Product should be a Product!')
        
        if type(seller) is Seller:
            self.__seller = seller
        else:
            raise ValueError('Seller should be a seller!')

        if type(customer) is Customer:
            self.__customer = customer
        else:
            raise ValueError('Customer should be a Customer!')

        self.__date = jdatetime.datetime.now()

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
    def seller(self):
        return self.__seller

    @product.setter
    def seller(self,value):
        if type(value) is Seller:
            self.__seller = value
        else:
            raise ValueError('Seller should be a Seller!')

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self,value):
        if type(value) is Customer:
            self.__customer = value
        else:
            raise ValueError('Customer should be a Customer!')

    @property
    def date(self):
        return self.__date

    def __str__(self):
        return '\n Product:\n' + str(self.product) + '\n Seller:\n' + str(self.seller) + '\n Customer:\n' + str(self.customer) + '\n Date:\n' + str(self.date)

# x = Product ('book' , 50000 , 15, ['good','nice'],[4,3,4,2])
# p1 = Product('book' , 50000 , 5, ['good','nice'], [4,3])
# p2 = Product('pen' , 5000 , 10, ['good','nice'], [4,2])

# s = Seller('Arezu','Kamrani','09121234567',a,1234567890,456789,1200,'seller',1243,[[p1,2],[p2,1]])
# s = Sale(p1,)