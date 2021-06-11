'''
This is a class defining a products in a shop.
This class includes shop product and their specifications.
You should notice that this class makes access to products easier.

Usage:
   1) Create a new product :
        p= product(ID, product_name, product_Price, product_discount)

   2) Print the product information:    
        print(p)
'''

class Product:
    def __init__(self, id, name, Price,  discount=0, comment_list=[], score=[]) :
        self.__id = id
        self.__name = name

        if  Price<=0 :
            raise ValueError('the Price for a product should be positive!')
        self.__Price = Price

        if  discount<0 or discount>=100:
            raise ValueError('the discount for a product should be in range [0,100).')
        self.__discount = discount

        self.__comment_list = comment_list

        score_list=[i for i in range(1,5+1) ]
        for i in score:
            if i not in score_list :
                raise ValueError('Score should be positive, integer and should not be more than five! ')
        self.__score = score
    
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
            raise ValueError('the Price for a product should be positive! ')
       self.__Price = value
  
    @property
    def discount(self): 
        return self.__discount

    @discount.setter
    def discount(self,value): 
        if  value<0 or value>=100:
            raise ValueError('the discount for a products should be in range [0,100).')
        self.__discount = value
    
    #getters
    @property
    def comment_list(self):
        cm = ''
        for i in range(0,len(self.__comment_list)-1):
            cm = cm + self.__comment_list[i] + ', '
        cm += self.__comment_list[-1]
        return cm
    
    @property
    def score(self):
        s = 0
        for i in self.__score:
            s += i
        return s/len(self.__score)


    def __str__(self):
        new_price=int(((100-self.discount)*self.Price)/100) 
        return '\n ID: {} \n name: {} \n Price: {} thousand toman  ==> discount: {} % ==> new Price: {} thousand toman \n Comments: {} \n average score: {} \n'\
            .format(self.ID,self.name, self.Price, self.discount,new_price, self.comment_list,self.score)
    

x = Product ( 'p123', 'book' , 50000 , 15, ['good','nice'],[4,3,4,2])
print(x)