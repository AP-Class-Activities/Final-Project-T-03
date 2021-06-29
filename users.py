from address import Address
class User:
    '''
    This class defines users in the main shop. 
    It contains the user's information. 
    Users contains sellers, customers and the users who just visit the main shop.
    The information consists of user's first name, last name, phone number, email, address, postal code, id, password and his/hers electronic wallet.
    This class helps the main shop to access users' information.
    The main shop needs this information to send the products to the customers who have buyed them.

    Usage:
        1) Create a new user:
           u = User(user_first_name, user_last_name, user_phone_number, user_adress, user_postal_code, user_id, user_password, user_electronic_wallet)
    
        2) print the user information:
           print(u)
           
    '''

    def __init__(self, first_name, last_name, phone_number, address, postal_code, password, electronic_wallet): # id , type
        
        self.__first_name = first_name
        self.__last_name = last_name

        if len(phone_number)!=11 or phone_number[0]!='0':
            raise ValueError('The phone number should have 11 digits and start with zero! ')
        self.__phone_number = phone_number

        if type(address) is not Address:
            raise ValueError('Address should be an Address!')
        self.__address = address

        if postal_code // (10**9) < 0 or postal_code // (10**9) > 10:
            raise ValueError('The postal code should have 10 digits! ')
        self.__postal_code = postal_code

        if len(str(password)) < 3 or len(str(password)) > 8:
            raise ValueError('The password should have between 4 and 8 characters.')
        self.__password = password

        if electronic_wallet < 0:
            raise ValueError('The electronic_wallet should be positive! ')
        self.__electronic_wallet = electronic_wallet

        # if type not in ['seller' , 'customer']:
        #     raise ValueError('type sholdb be seller or customer. ')
        # self.__type = type

        # if id // (10**5) < 0 or id // (10**5) > 10:
        #     raise ValueError('The id should have 6 digits. ')
        # self.__id = id

    #setters and getters
    @property
    def first_name(self): 
        return self.__first_name

    @first_name.setter
    def first_name(self,value): 
        self.__first_name = value
    
    @property
    def last_name(self): 
        return self.__last_name

    @last_name.setter
    def last_name(self,value): 
        self.__last_name = value
    
    @property
    def  phone_number(self): 
        return self.__phone_number

    @phone_number.setter
    def  phone_number(self,value): 
       if len(value)!=11 or value[0]!='0':
            raise ValueError('The phone number should have 11 digits and start with zero! ')
       self.__phone_number = value

    @property
    def address(self): 
        return self.__address

    @address.setter
    def address(self,value): 
        if type(value) is not Address:
            raise ValueError('Address should be an Address!')
        self.__address = value
    
    @property
    def  postal_code(self): 
        return self.__postal_code

    @postal_code.setter
    def  postal_code(self,value): 
      if value // (10**9) < 0 or value // (10**9) > 10:
            raise ValueError('The postal code should have 10 digits! ')
      self.__postal_code = value
   
    @property
    def password(self): 
        return self.__password

    @password.setter
    def  password(self,value):
        if len(str(value)) < 3 or len(str(value)) > 8:
            raise ValueError('The password should have between 4 and 8 characters. ')
        self.__password = value

    @property
    def electronic_wallet(self): 
        return self.__electronic_wallet

    @electronic_wallet.setter
    def  electronic_wallet(self,value):
        new_value = self.__electronic_wallet + value
        if new_value < 0:
            raise ValueError('The electronic_wallet should be positive! ')
        self.__electronic_wallet = new_value


    
    def __str__(self): 
        return '\n first name: {}  \n last name: {}  \n phone number: {}  \n address: {}  \n postal code: {}  \n password: {}  \n electronic_wallet: {} \n'\
            .format(self.first_name,self.last_name, self.phone_number, self.address, self.postal_code, self.password, self.electronic_wallet)

#example client code:
# u = User('Arezu','Kamrani','09121234567','Rasht',1234567890,456789,1200)
# print(u)

import jdatetime
# from date import Date 
# from sale import Sale
from Products import  Product
from random import randint
# import Seller

class Seller(User):
    '''
    This is a class for defining a seller.
    Seler is a kind of User.
    Each seller has a list of products and wants to sell them.
    Each Seller has a list of scores.
    A seller can add new products to his/her list of products.

    '''
    def __init__(self, first_name, last_name, phone_number, address, postal_code, password, electronic_wallet, id, product_stock = [], score = []):
        super(Customer,self).__init__(first_name, last_name, phone_number, address, postal_code, password, electronic_wallet, type, id)
    
        # x = randint(100000,999999)
        # while 'PR' + str(x) in ID_list:   # ID_list should be made by ID_file :(
        #     x = randint(100000,999999)
        # self.__id = 'PR' + str(x)


        for i in product_stock:     # product_stock = [[product1, stock1],[product2, stock2],...]
            if type(i[0]) is not Product or i[1]< 0:
                raise ValueError('Product Stock should be a list products and their stocks! Stocks should not be negative!')
        self.__product_stock = product_stock

        score_list=[i for i in range(0,5+1) ]
        for i in score:
            if i not in score_list :
                raise ValueError('Score should be positive, integer and should not be more than five! ')
        self.__score = score
    
    # getter:
    
    # @property
    # def ID(self):
    #     return self.__id

    # setter and getter:

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        score_list=[i for i in range(0,5+1) ]
        if value not in score_list :
            raise ValueError('Score should be positive, integer and should not be more than five! ')
        self.__score = self.score + [value]

    @property
    def product_stock(self):
        return self.__product_stock

    def add_product(self,value):  # value = [product1,stock1]
        if type(value[0]) is not Product:
           raise ValueError('Product Stock should be a list products and their stocks!')
        for i in self.product_stock:
            if i[0] == value[0]:
                if i[1] + value[1] < 0:
                    raise ValueError('Stock can not be negative!')
                else:
                    j = [i[0],i[1] + value[1]]
                    self.__product_stock = self.product_stock.remove(i) + j
        if value[1] < 0:
            raise ValueError('stock should be positive!')
        self.__product_stock = self.product_stock + [value] 

        
    def average_score(self):
        s = 0
        for i in self.score:
            s += i
        return s/(len(self.score))

    def product_str(self):
        s = ''
        for i in self.product_list:
            s = s + 'Product:' + str(i[0]) + 'Stock:' + str(i[1]) + '\n'
        return s

    def __str__(self):
        return super(Seller,self).__str__() + '\n' + self.product_str()   # + 'ID: ' + self.ID 

# a = Address('Guian','Rasht','Golsar','123','25','4')
# u = User('Arezu','Kamrani','09121234567',a,1234567890,456789,1200)
# s = Seller('Arezu','Kamrani','09121234567',a,1234567890,456789,1200,[[p1,2],[p2,1]])
# s = Seller(u,[p1,p2])
# print(s)


class Customer(User):
    '''
    This class defines customers in the main shop.
    Customer is a user.
    In this class we can see that each customer has a favorite list and can add products to this list or delete them from it.
    Each customer has a shopping bag and can add products to or delete them from it.
    Each customer access to the Product class, date class and sale class.
    This class allows each customers to see his/her buy history, favorite list and shopping bag.
    Each customer will be only able to comment for the produst he/she has buyed.

    Usage:
        1) Create a new customer:
           c = customer(customer_first_name, customer_last_name, customer_phone_number, customer_adress, customer_postal_code, user_password, customer_electronic_wallet, customer_type, customer_id, favorite_list=[], shopping_bag=[], buy_history=[])
    
        2) print the customer information:
           print(c)
    '''
    def __init__(self, first_name, last_name, phone_number, address, postal_code, password, electronic_wallet, favorite_list = [], shopping_bag = [], Product=[], Sale=[], Date=[]): # , buy_history = []
        super(Customer,self).__init__(first_name, last_name, phone_number, address, postal_code, password, electronic_wallet, type, id)
        
        # x = randint(100000,999999)
        # while 'CU' + str(x) in ID_list:   # ID_list should be made by ID_file :(
        #     x = randint(100000,999999)
        # self.__id = 'CU' + str(x)
        
        for i in favorite_list:
            if type(i) is not Product:
                raise ValueError('Favorite List should be a list of lists of products!')
        fl =[]
        for i in favorite_list:
            if i not in fl:
                fl.append(i)
        self.__favorite_list = fl  # favorite_list = [product1,product2,...]
        
        for i in shopping_bag:
            if type(i[0]) is not Product or type(i[1]) is not Seller:
                raise ValueError('Shopping Bag should be a list of lists of products and their Sellers!')
        sb = []
        for i in shopping_bag:
            if [i[0],i[1],0] not in sb:
                sb = sb + [i[0],i[1],0]
        for i in shopping_bag:
            for j in sb:
                if i[0] == j[0] and i[1] == j[1]:
                    j[2] += i[2]
        self.__shopping_bag = sb # shopping_bag = [[product1, seller1, number1],...]

        # for i in buy_history: 
        #     for j in i:
        #         if type(j) is not Sale:
        #              raise ValueError('Buy History should be a list of lists of sales!')
        #         for k in i:
        #             if j.customer != self or j.date.year != k.date.year or j.date.month != k.date.month or j.date.day != k.date.day or j.date.hour != k.date.hour or j.date.minute != k.date.minute:
        #                 raise ValueError('Each item in the buy history should be a list of sales with the same customer(self) and date!')
        # self.__buy_history = buy_history # buy_history =[[sale1,sale2,...],[sale'1,sale'2,...],...]

    #getters

    # @property
    # def ID(self):
    #     return self.__id

    @property
    def favorite_list(self):
        return self.__favorite_list

    @property
    def shopping_bag(self):
        return self.__shopping_bag

    # @property
    # def buy_history(self):
    #     return self.__buy_history
 
    def add_favorite_list(self,value):
        if value is not Product:
                raise ValueError('You should enter a Product.')
        elif value in self.favorite_list:
            return
        self.__favorite_list = self.favorite_list + [value]
 
    def sub_favorite_list(self,value):
        if value is not Product:
                raise ValueError('You should enter a Product.')
        elif value not in self.favorite_list:
            return
        self.__favorite_list = self.favorite_list.remove(value)
 
    def modify_shopping_bag(self,value):
        if type(value[0]) is not Product or type(value[1]) is not Seller:
                raise ValueError('You should enter a list of a Product and its Seller here.')
        for i in self.shopping_bag:
            if i[0] == value[0] and i[1] == value[1]:
                if i[2] + value[2] < 0:
                    raise ValueError('The number of a product in shopping bag can not be negative!')
                elif i[2] + value[2] == 0:
                    self.__shopping_bag = self.shopping_bag.remove(i)
                else:
                   j = [i[0], i[1], i[2] + value[2]]
                   self.__shopping_bag = self.shopping_bag.remove(i) + j
        if value[2] < 0:
            raise ValueError('The number of a product in shopping bag should be positive')
        elif value[2] == 0:
            return
        self.__shopping_bag = self.shopping_bag + [value]

    # def add_buy_history(self,value):
    #     for i in value:
    #             if type(i) is not Sale:
    #                  raise ValueError('Buy History should be a list of sales!')
    #             for j in value:
    #                 if i.customer != self or i.date.year != j.date.year or i.date.month != j.date.month or i.date.day != j.date.day or i.date.hour != j.date.hour or i.date.minute != j.date.minute:
    #                     raise ValueError('Each itemin the buy history should be a list of sales with the same customer(self) and date!')
    #     self.__buy_history = self.buy_history + [value] 

    # def buy(self,buy_list =[], date = jdatetime.datetime.now()): # buy_list = [[product,seller]]
    #     for i in buy_list:
    #         if i[0].stock < buy_list.count(i):    
    #             return 'There is not enough {}'\
    #                 .format(i.name + i)     # i ???
    #         total_price = 0
    #         for i in buy_list:
    #             total_price += i.Price
    #         if self.electronic_wallet > total_price or self.electronic_wallet == total_price:
    #             self.electronic_wallet((-1)*total_price)
    #             b_h =[]
    #             for i in buy_list:
    #                 s = Sale(i,i[1],self)
    #                 b_h.append(s)
    #                 i.stock(-1) 
    #             self.add_buy_history(b_h)    
    #         else: 
    #             print('You do not have enough money.')
    #         return


    # def comment(self,element,value):
    #     for i in self.buy_history:
    #         for j in i:
    #             if element in j:
    #                 element.comment(self.first_name + ' ' + self.last_name + ': ' + value)
    #                 return
    #     raise ValueError('You can only comment for the products you have bought before!')
        
    # def rate(self,element,value):
    #     for i in self.buy_history:
    #         for j in i:
    #             if element in j:
    #                 element.score(value)
    #                 j.seller.score(value)
    #                 return
    #     raise ValueError('You can only rate the products you have bought before!')


    def str_favorite_list(self):
        fl = ''
        for i in self.favorite_list:
            fl += str(i)
        return fl

    def str_shopping_bag(self):
        sb = ''
        for i in self.shopping_bag:
            sb = sb + 'Product:' + str(i[0]) + 'Seller:' + str(i[1]) + 'Number:' + str(i[2]) + '\n'
        return sb

    # def str_buy_history(self):
    #     bh = ''
    #     t = '______________________________________________________________________________________________________________\n'
    #     for i in self.buy_history:
    #         for j in i:
    #            bh += str(i)
    #         bh += t
    #     return bh


    def __str__(self):
        s ='________________________________________________________________________________________________________________\n'
        f_l = '\n favorite list: \n {}'.format(self.str_favorite_list())
        s_b = '\n shopping bag: \n {}'.format(self.str_shopping_bag())
        # b_h = '\n buy history: \n {}'.format(self.str_buy_history())
        return super(Customer,self).__str__() + s + f_l + s + s_b + s     # + b_h


p1 = Product(123456, 'book' , 50000 , 5, ['good','nice'], [4,3])
p2 = Product(987654, 'pen' , 5000 , 10, ['good','nice'], [4,2])
p3 = Product(654237, 'pencil' , 2000 , 2, ['good','nice','soft'], [4,3,5])
p4 = Product(528643, 'eraser' , 5000 , 15, ['good','soft'], [4,3,1])
p5 = Product(525613, 'ruler' , 10000 , 20, ['good','nice','long'], [4,3,1])
s1 = Seller('Arezu','Kamrani','09121234567','Rasht',1234567890,456789,1200,'seller',123456,[[p1,3],[p2,5]])
c = Customer('Arezu','Kamrani','09121234567','Rasht',1234567890,456789,1200,'customer',123456,[p1,p2,p3],[[p1,s1,2]])
# s2 = Sale(p1,s1,c)
# c.buy_history(s2)
print(c) 
# print(type(c))
# c.comment(p5,'very good')
# print(p5.str_comment)

