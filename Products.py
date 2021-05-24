'''
This is a class defining the product  in a shop.
This class includes shop product and product specifications.
You should notice that this class makes access to products easier.


Authors:
Email:


Usage:
   1) Create a new product :
        p= product(ID, product_name, product_Price)

   2) Print the product information:    
        print(p)
'''

class Products:
    def __init__(self, id, name, Price) :
        self.__id = id
        self.__name = name
        self.__Price = Price