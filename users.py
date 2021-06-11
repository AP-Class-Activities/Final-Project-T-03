class user:
    '''
    This class defines users in the main shop. 
    It contains the user's information. 
    Users contains sellers, customers and the users who just visit the main shop.
    The information consists of user's first name, last name, phone number, email, address, postal code, id, password and his/hers electronic wallet.
    This class helps the main shop to access users' information.
    The main shop needs this information to send the products to the customers who have buyed them.

    Usage:
        1) Create a new user:
           u = user(user_first_name, user_last_name, user_phone_number, user_adress, user_postal_code, user_id, user_password, user_electronic_wallet)
    
        2) print the user information:
           print(u)
    '''

    def __init__(self, first_name, last_name, phone_number, address, postal_code, password, electronic_wallet, type, id):
        self.__first_name = first_name
        self.__last_name = last_name

        if len(phone_number)!=11 or phone_number[0]!='0':
            raise ValueError('The phone number should have 11 digits and start with zero! ')
        self.__phone_number = phone_number

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

        if type not in ['seller' , 'customer']:
            raise ValueError('type sholdb be seller or customer. ')
        self.__type = type

        if id // (10**5) < 0 or id // (10**5) > 10:
            raise ValueError('The id should have 6 digits. ')
        self.__id = id
    
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
        if value < 0:
            raise ValueError('The electronic_wallet should be positive! ')
        self.__electronic_wallet = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self,value):
        if type not in ['seller' , 'customer']:
            raise ValueError('type sholdb be seller or customer. ')
        self.__type = type
   
    @property
    def ID(self): 
        if self.__type == 'seller':
            return 'SL'+str(self.__id)
        elif self.__type == 'customer':
            return 'CU'+str(self.__id)

    @ID.setter
    def  ID(self,value):
        if value // (10**5) < 0 or value // (10**5) > 10:
            raise ValueError('The id should have 6 digits. ')
        self.__id = value
    
    def __str__(self): 
        return '\n first name: {}  \n last name: {}  \n phone number: {}  \n address: {}  \n postal code: {}  \n password: {}  \n electronic_wallet: {} \n user type: {} \n user id: {} \n'\
            .format(self.first_name,self.last_name, self.phone_number, self.address, self.postal_code, self.password, self.electronic_wallet, self.type, self.ID)

#example client code:
# u = user('Arezu','Kamrani','09121234567','Rasht',1234567890,456789,1200,'seller',1243)
# print(u)

from Products import  Product
class customer(user):
    '''
    This class defines customers in the main shop.
    Customer is a user.
    In this class we can see that each customer has a favorite list and can add products to this list or delete them from it.
    Each customer has a shopping bag and can add products to or delete them from it.
    Each customer access to the produts.
    This class allows each customers to see his/her buy history, favorite list and shopping bag.
    Each customer will be only able to comment for the produst he/she has buyed.

    Usage:
        1) Create a new customer:
           c = customer(customer_first_name, customer_last_name, customer_phone_number, customer_adress, customer_postal_code, user_password, customer_electronic_wallet, customer_type, customer_id, favorite_list=[], shopping_bag=[], buy_history=[])
    
        2) print the customer information:
           print(c)
    '''
    def __init__(self, first_name, last_name, phone_number, address, postal_code, password, electronic_wallet, type, id, favorite_list, shopping_bag, buy_history, Product=[]):
        super(customer,self).__init__(first_name, last_name, phone_number, address, postal_code, password, electronic_wallet, type, id)
        
        self.__favorite_list = favorite_list
        self.__shopping_bag = shopping_bag
        self.__buy_history = buy_history
        self.__Product=Product

    @property
    def favorite_list(self):
        fl = ''
        for i in self.__favorite_list:
            fl += i
        return fl

    @property
    def shopping_bag(self):
        sb = ''
        for i in self.__shopping_bag:
            sb += i
        return sb

    @property
    def buy_history(self):
        bh = ''
        for i in self.__buy_history:
            bh += i
        return bh

    @property
    def Product(self): 
        return self.__Product
      
    def __str__(self):
        return super(customer,self).__str__() + '  favorite list: {}  \n shopping bag:{}  \n buy history: {}'.format(self.favorite_list, self.shopping_bag, self.buy_history)
  
    def __str__(self):
        p = ''
        p += '\n\n_____________________________________________Product__________________________________________________\n\n'
        for i in self.Product: 
            p += '%p\n'%(i)
        return p


p1 = Product('p123', 'book' , 50000 , 5, ['good','nice'], [4,3])
p2 = Product('s123', 'pen' , 5000 , 10, ['good','nice'], [4,2])
p3 = Product('pv23', 'pencil' , 2000 , 2, ['good','nice','soft'], [4,3,5])
p4 = Product('p1o3', 'eraser' , 5000 , 15, ['good','soft'], [4,3,1])
p5 = Product('p12ff', 'ruler' , 10000 , 20, ['good','nice','long'], [4,3,1])
c = customer('Arezu','Kamrani','09121234567','Rasht',1234567890,456789,1200,'customer',123456,[p1,p2,p3],[p1,p4],[p5,p2])
print(c) 