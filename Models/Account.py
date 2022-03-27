

#This class describes a Personal account in the system
#A user Account will be able to file their taxes, compute their net income after taxes
#A personal  Account object will store the filers name, province, social insurance number
#file tax return etc.
#province is a 2 character string repersenting the province 
class Account: 
    
    def __init__(self,firstName,lastName,prov,sin, birthDate) -> None:
        self.__firstName=firstName
        self.__lastName=lastName
        self.__prov=prov
        self.__sin=sin
        self.__birthDate=birthDate

    
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getFullName(self):
        return self.__firstName + ' '+self.__lastName
    
    def getProvince(self):
        return self.__prov

    def getSin(self):
        return self.__sin
    def getBirthDate(self):
        return self.__birthDate