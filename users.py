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
           u = User(user_first_name, user_last_name, user_sexuality, user_phone_number, user_adress, user_postal_code, user_password, user_electronic_wallet)
    
        2) print the user information:
           print(u)
           
    '''

    def __init__(self, first_name, last_name, sexuality, phone_number, address, postal_code, password, electronic_wallet):
        
        for i in first_name:
            if i in [str(j) for j in range(0,10)]:
                raise ValueError('First Name does not include number.')
        self.__first_name = first_name

        for i in last_name:
            if i in [str(j) for j in range(0,10)]:
                raise ValueError('Last Name does not include number.')
        self.__last_name = last_name

        if sexuality not in ['Man', 'Woman']:
            raise ValueError('Sexuality should be Man or Woman!')
        self.__sexuality = sexuality

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

    #setters and getters
    @property
    def first_name(self): 
        return self.__first_name

    @first_name.setter
    def first_name(self,value): 
        for i in value:
            if i in [str(j) for j in range(0,10)]:
                raise ValueError('First Name does not include number.')
        self.__first_name = value
    
    @property
    def last_name(self): 
        return self.__last_name

    @last_name.setter
    def last_name(self,value): 
        for i in value:
            if i in [str(j) for j in range(0,10)]:
                raise ValueError('Last Name does not include number.')
        self.__last_name = value
    
    @property
    def sexuality(self):
        return self.__sexuality

    @sexuality.setter
    def sexuality(self,value):
        if value not in ['Man', 'Woman']:
            raise ValueError('Sexuality should be Man or Woman!')
        self.__sexuality = value

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
        return '\n first name: {}  \n last name: {}  \n Sexuality: {}  \n phone number: {}  \n address: {}  \n postal code: {}  \n password: {}  \n electronic_wallet: {} \n'\
            .format(self.first_name,self.last_name, self.sexuality, self.phone_number, self.address, self.postal_code, self.password, self.electronic_wallet)

#example client code:
# u = User('Arezu','Kamrani', 'Woman','09121234567','Rasht',1234567890,456789,1200)
# print(u)

from Products import  Product

class Seller(User):
    '''
    This is a class for defining a seller.
    Seler is a kind of User.
    Each seller has a list of products and wants to sell them.
    Each Seller has a list of scores.
    A seller can add new products to his/her list of products.

    Usage:
         1) Create a Seller:
            s = Seller(first_name, last_name, sexuality, phone_number, address, postal_code, password, electronic_wallet)
         2) Print a Seller:
            print(s)
        3) The Seller can add Products to or delete products from his/her product_stock:
           s.product_stock(value)  value = [product1,stock1]

    '''
    def __init__(self, first_name, last_name, sexuality, phone_number, address, postal_code, password, electronic_wallet):
        super(Seller,self).__init__(first_name, last_name, sexuality, phone_number, address, postal_code, password, electronic_wallet)
  
        self.__product_stock = []    # product_stock = [[product1, stock1],[product2, stock2],...]
        
        self.__score = []
    

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
                elif i[1] + value[1] == 0:
                    self.__product_stock = self.product_stock.remove(i)
                    return
                else:
                    j = [i[0],i[1] + value[1]]
                    self.__product_stock = self.product_stock.remove(i) + j
                    return
        if value[1] < 0:
            raise ValueError('stock should be positive!')
        self.__product_stock = self.product_stock + [value] 

        
    def average_score(self):
        s = 0
        for i in self.score:
            s += i
        if len(self.score) == 0:
            return ''
        return s/(len(self.score))

    def product_str(self):
        s = ''
        for i in self.product_list:
            s = s + 'Product:' + str(i[0]) + 'Stock:' + str(i[1]) + '\n'
        return s

    def __str__(self):
        return super(Seller,self).__str__() + '\n' + self.product_str() + '\n' + 'Average Score:' + str(self.average_score())

# a = Address('Guian','Rasht','Golsar','123','25','4')
# u = User('Arezu','Kamrani','Woman', '09121234567',a,1234567890,456789,1200)
# s = Seller('Arezu','Kamrani','Woman' ,'09121234567',a,1234567890,456789,1200)
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
           c = Customer(customer_first_name, customer_last_name, customer_sexuality, customer_phone_number, customer_adress, customer_postal_code, user_password, customer_electronic_wallet)
    
        2) print the customer information:
           print(c)
        
        3) The Customer can add products to of delete products from his/her shopping_bag:
           c.modify_shopping_bag(value)  value = [product1,seller1,number1]

        4) The Customer can add product to his/her favorite_list:
           c.add_favorite_list(value)  value is a product

        5) The customer can delete a product from his/her favorite_list:
           c.sub_favorite_list(value)  value is a product
    '''
    def __init__(self, first_name,sexuality, last_name, phone_number, address, postal_code, password, electronic_wallet):
        super(Customer,self).__init__(first_name, last_name, sexuality, phone_number, address, postal_code, password, electronic_wallet)

        self.__favorite_list = []   # favorite_list = [product1,product2,...]

        self.__shopping_bag = []  # shopping_bag = [[product1, seller1, number1],...]


    #getters

    @property
    def favorite_list(self):
        return self.__favorite_list

    @property
    def shopping_bag(self):
        return self.__shopping_bag

    # @property

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
                    return
                else:
                   j = [i[0], i[1], i[2] + value[2]]
                   self.__shopping_bag = self.shopping_bag.remove(i) + j
                   return
        if value[2] < 0:
            raise ValueError('The number of a product in shopping bag should be positive')
        elif value[2] == 0:
            return
        self.__shopping_bag = self.shopping_bag + [value]

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

    def __str__(self):
        s ='________________________________________________________________________________________________________________\n'
        f_l = '\n favorite list: \n {}'.format(self.str_favorite_list())
        s_b = '\n shopping bag: \n {}'.format(self.str_shopping_bag())
        return super(Customer,self).__str__() + s + f_l + s + s_b + s    


# p1 = Product('book' , 50000 , 5, ['good','nice'])
# p2 = Product('pen' , 5000 , 10, ['good','nice'])
# p3 = Product('pencil' , 2000 , 2, ['good','nice','soft'])
# p4 = Product('eraser' , 5000 , 15, ['good','soft']])
# p5 = Product('ruler' , 10000 , 20, ['good','nice','long'])
# s1 = Seller('Arezu','Kamrani','Woman', '09121234567','Rasht',1234567890,456789,1200,'seller',123456)
# c = Customer('Arezu','Kamrani','Woman', '09121234567','Rasht',1234567890,456789,1200,'customer',123456)
# print(c) 
# print(type(c))
