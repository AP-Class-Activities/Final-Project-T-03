'''
This is a class defining a products in a shop.
This class includes shop product and their specifications.
You should notice that this class makes access to products easier.

Authors:fatemeh mohammaddost

Usage:
   1) Create a new product :
        p= product(ID, product_name, product_Price)

   2) Print the product information:    
        print(p)
'''

class Product:
    def __init__(self, id, name, Price,  discount=0) :
        self.__id = id
        self.__name = name

        if  Price<=0 :
            raise ValueError('the Price for a product should be positive')
        self.__Price = Price

        if  discount<0 or discount>=100:
            raise ValueError('the discount for a product should be in range [0,100)')
        self.__discount = discount
    
    #setters and getters
    @property
    def ID(self): 
        return self.__id
    
    @ID.setter
    def ID(self,value): 
        self.__id = value

    @property
    def name(self): 
        return self.__name

    @name.setter
    def name(self,value): 
        self.__name = value

    @property
    def Price(self): 
        return self.__Price

    @Price.setter
    def Price(self,value): 
       if  value<=0 :
            raise ValueError('the Price for a product should be positive')
       self.__Price = value
  
    @property
    def discount(self): 
        return self.__discount

    @discount.setter
    def discount(self,value): 
        if  value<0 or value>=100:
            raise ValueError('the discount for a products should be in range [0,100)')
        self.__discount = value

    def __str__(self):
        new_price=((100-self.discount)*self.Price)/100 
        return '\n ID: {} \n name: {} \n Price: {}  ==> discount: {}  ==> new Price: {} \n'\
            .format(self.ID,self.name, self.Price, self.discount,new_price)
        

x = Product ( 'p123', 'book' , 50000 , -5)

print(x)