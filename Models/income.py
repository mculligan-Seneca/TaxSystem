from Models.taxobject import TaxObject


#this class repersents the taxable  income 
class Income(TaxObject):
    

    def __init__(self,value,description):
        TaxObject.__init__(self,value,description)


    
 

    def __add__(self,x)->float:
        if isinstance(x,TaxObject) or isinstance(x,float):
            return x+self.getTaxableIncome()
     

    def getTaxableIncome(self):
       return super().getAmount()
    
    
     
