'''
   This class is for adress.
   
   Usage:
      1) Create a new address:
         a = Address(province,city,street,alley,plaque,unit)
      2) Print the address information:
         print(a)
'''

class Address:
    def __init__(self, province, city, street, alley, plaque, unit):

        for i in province:
            if i in [str(j) for j in range(0,10)]:
                raise ValueError('Province does not include number.')
        self.__province = province

        for i in city:
            if i in [str(j) for j in range(0,10)]:
                raise ValueError('City does not include number.')
        self.__city = city

        self.__street = street
        self.__alley = alley
        self.__plaque = plaque
        self.__unit = unit

    # setter and getter
   
    @property
    def province(self):
        return self.__province

    @province.setter
    def province(self,value):
        for i in value:
            if i in [str(j) for j in range(0,10)]:
                raise ValueError('Province does not include number.')
        self.__province = value
   
    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self,value):
        for i in value:
            if i in [str(j) for j in range(0,10)]:
                raise ValueError('City does not include number.')
        self.__city = value
   
    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self,value):
        self.__street = value

   
    @property
    def alley(self):
        return self.__alley

    @alley.setter
    def alley(self,value):
        self.__alley = value

       
    @property
    def plaque(self):
        return self.__plaque

    @plaque.setter
    def plaque(self,value):
        self.__plaque = value
   
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self,value):
        self.__unit = value

    def __str__(self):
        return 'Province: {}, City: {}, Street: {}, Alley: {}, Plaque: {}, Unit: {}'.\
            format(self.province, self.city, self.street, self.alley, self.plaque, self.unit)