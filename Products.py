'''
This is a class defining a products in a shop.
This class includes shop product and their specifications.
You should notice that this class makes access to products easier.

Usage:
   1) Create a new product :
        p= product(ID, product_name, product_Price, product_discount, comment_list, score)

   2) Print the product information:    
        print(p)
        
'''

from address import Address

class Product:
    def __init__(self, id, name, Price, discount=0, comment_list=[], score=[]) : #, stock=0
        if id//(10**5) == 0 or id//(10**5) > 10:
            raise ValueError('id should have 6 digits.')
        self.__id = id
        self.__name = name

        if  Price<=0 :
            raise ValueError('the Price for a product should be positive!')
        self.__Price = Price

        if  discount<0 or discount>=100:
            raise ValueError('the discount for a product should be in range [0,100).')
        self.__discount = discount

        self.__comment_list = comment_list

        score_list=[i for i in range(0,5+1) ]
        for i in score:
            if i not in score_list :
                raise ValueError('Score should be positive, integer and should not be more than five! ')
        self.__score = score

    #setters and getters
    @property
    def ID(self): 
        return 'PR' + str(self.__id)
    
    @ID.setter
    def ID(self,value): 
        if value//(10**5) == 0 or value//(10**5) > 10:
            raise ValueError('id should have 6 digits.')
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

    @property
    def comment_list(self):
        return self.__comment_list

    @comment_list.setter
    def comment_list(self,value):
        self.__comment_list = self.comment_list + [value]

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        score_list=[i for i in range(0,5+1) ]
        if value not in score_list :
            raise ValueError('Score should be positive, integer and should not be more than five! ')
        self.__score = self.score + [value]

    def str_comment(self):
        cm = ''
        for i in range(0,len(self.comment_list)-1):
            cm = cm + self.comment_list[i] + ', '
        cm += self.comment_list[-1]
        return cm
    
    def average_score(self):
        s = 0
        for i in self.score:
            s += i
        return s/(len(self.score))
  
    def new_price(self):
        return int(((100-self.discount)*self.Price)/100)

    def __str__(self): 
        return '\n ID: {} \n name: {} \n Price: {} toman  ==> discount: {} % ==> new Price: {} toman \n Comments: {} \n average score: {} \n'\
            .format(self.ID,self.name, self.Price, self.discount,self.new_price(), self.str_comment(),self.average_score())
    
# example client code:
# x = Product ( 123456, 'book' , 50000 , 15, ['good','nice'],[4,3,4,2])
# print(x)
# x.add_comment('useful')
# print(x.str_comment())
