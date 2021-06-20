'''
This class shows the time.
This class help the main shop to classify the list of each seller's daily purchase.
By using this class we can find the time between two date.

Usage:
   1) Create a new date:
      d = Date(year,month,day,hour,minute,second)
 
   2) Print its information:
      print(d)
'''

class Date:
    def __init__(self, year, month, day, hour, minute, second):

        if year not in [i for i in range(1396,1405)]:
            raise ValueError('Year should be between 1396 and 1404.')
        self.__year = year

        if month not in [i for i in range(1,13)]:
            raise ValueError('Month should be between 1 and 12.')
        self.__month = month

        if month in [i for i in range(1,7)] and day not in [i for i in range(1,32)]:
            raise ValueError('Day should be between 1 and 31.')
        elif month in [i for i in range(7,12)] and day not in [i for i in range(1,31)]:
            raise ValueError('Day shoud be between 1 and 30')
        elif month == 12 and day not in [i for i in range(1,30)]:
            raise ValueError('Day should be between 1 and 29.')
        self.__day = day

        if hour not in [i for i in range(0,24)]:
            raise ValueError('Hour should be between 0 and 23.')
        self.__hour = hour

        if minute not in [i for i in range(0,60)]:
            raise ValueError('Minute should be between 0 and 59.')
        self.__minute = minute

        if second not in [i for i in range(0,60)]:
            raise ValueError('Second should be between 0 and 59.')
        self.__second = second

    #setter and getter

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self,value):
        if value not in [i for i in range(1396,1405)]:
            raise ValueError('Year should be between 1396 and 1404.')
        self.__year = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self,value):
        if value not in [i for i in range(1,13)]:
            raise ValueError('Month should be between 1 and 12.')
        self.__month = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self,value):
        if month in [i for i in range(1,7)] and value not in [i for i in range(1,32)]:
            raise ValueError('Day should be between 1 and 31.')
        elif month in [i for i in range(7,12)] and value not in [i for i in range(1,31)]:
            raise ValueError('Day shoud be between 1 and 30')
        elif month == 12 and value not in [i for i in range(1,30)]:
            raise ValueError('Day should be between 1 and 29.')
        self.__day = value   

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self,value):
        if value not in [i for i in range(0,24)]:
            raise ValueError('Hour should be between 0 and 23.')
        self.__hour = value

    @property
    def minute(self):
        return self.__minute
        
    @minute.setter
    def minute(self,value):
        if value not in [i for i in range(0,60)]:
            raise ValueError('Minute should be between 0 and 59.')
        self.__minute = value

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self,value):
        if value not in [i for i in range(0,60)]:
            raise ValueError('Second should be between 0 and 59.')
        self.__second = value


    def __str__ (self):
        return '\n {}/{}/{} \n {}:{}:{} \n'\
        .format(self.year,self.month,self.day,self.hour,self.minute,self.second)

d = Date(1398,6,16,12,54,36)
print(d)