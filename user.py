'''
This class defines users in the main shop. 
It contains the user's information. 
Users contains sellers, customers and the users who just visit the main shop.
The information consists of user's first name, last name, phone number, email, address, postal code, id, password and his/hers electronic wallet.
This class helps the main shop to access users' information.
The main shop needs this information to send the products to the customers who have buyed them.

Authors: Niloofar Askari Masouleh and fatemeh mohammaddost

Usage:
    1) Create a new user:
        u = user(user_first_name, user_last_name, user_phone_number, user_address, user_postal_code, user_id, user_password, user_electronic_wallet)
    
    2) print the user information:
        print(u)

'''

class user:
    def __init__(self, first_name, last_name, phone_number, address, postal_code, id, password, electronic_wallet = 0):
        self.__first_name = first_name
        self.__last_name = last_name

        if phone_number % (10**9)!=9:
            raise ValueError('The phone number should have 10 digits and start with 9')
        self.__phone_number = phone_number

        self.__address = address

        if postal_code % (10**9) > 0 and postal_code % (10**9) <10:
            raise ValueError('The postal code should have 10 digits')
        self.__postal_code = postal_code

        if id % (10**5) > 0 and id % (10**5) < 10:
            raise ValueError('The id should have 6 digits')
        self.__id = id

        if len(password) < 3 or len(password) > 8:
            raise ValueError('The password should have between 4 and 8 characters')
        self.__password= password

        if electronic_wallet < 0:
            raise ValueError('The electronic_wallet should be positive')
        self.__electronic_wallet = electronic_wallet
    
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
       if value % (10**9)!=9:
            raise ValueError('The phone number should have 10 digits and start with 9')
       self.__phone_number = value

    @property
    def address(self): 
        return self.__address

    @address.setter
    def address(self,value): 
        self.__address = value
 
    
    @property
    def id(self): 
        return self.__id

    @id.setter
    def id(self,value): 
        self.__id = value
 
    @property
    def  postal_code(self): 
        return self.__postal_code

    @postal_code.setter
    def  postal_code(self,value): 
      if value % (10**9) > 0 and value % (10**9) <10:
            raise ValueError('The postal code should have 10 digits')
        self.__postal_code = value
    
    @property
    def id(self): 
        return self.__id

    @id.setter
    def  id(self,value):
        if value % (10**5) > 0 and value % (10**5) < 10:
            raise ValueError('The id should have 6 digits')
        self.__id = value
   
    @property
    def password(self): 
        return self.__password

    @password.setter
    def  password(self,value):
        if len(value) < 3 or len(value) > 8:
            raise ValueError('The password should have between 4 and 8 characters')
        self.__password = value

    @property
    def electronic_wallet(self): 
        return self.__electronic_wallet

    @electronic_wallet.setter
    def  electronic_wallet(self,value):
        if value < 0:
            raise ValueError('The electronic_wallet should be positive')
        self.__electronic_wallet = value

    def __str__(self): 
        return 'first_name: {}   , last_name: {}    , phone_number: {}   , address: {}   , postal_code: {}   , id: {}    , password: {}  , electronic_wallet: {} '\
            .format(self.first_name,self.last_name, self.phone_number, self.address, self.postal_code, self.id, self.password, self.electronic_wallet)