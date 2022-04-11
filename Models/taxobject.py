

#could be a deductable or a form of income

class TaxObject:



    def __init__(self,value:float,description):
        self.__amount=value
        self.__description=description


    
    def getDescription(self)->float:
        return self.__description
    def getAmount(self)->float:
        return self.__amount

    def __add__(self,x)->float:
        if isinstance(x,TaxObject) or isinstance(x,float):
            return x+self.__amount
     