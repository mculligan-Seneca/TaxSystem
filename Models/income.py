from Models.taxobject import TaxObject


#this class repersents the taxable  income 
class Income(TaxObject):
    

    def __init__(self,value,description):
        TaxObject.__init__(self,value,description)


    
 

    
     

    def getTaxableIncome(self):
       return super().getAmount()
    
    
     
