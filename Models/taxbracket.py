import numpy as np

#TaxBrackets class stores the data of the different rates of taxed to be supplied based on income
#income tax bracket
class TaxBracket:
   
  

       
    #init function expects a  file name with the format  lower_bracket,upper_bracket,rate%
    def __init__(self,bracketFile):

         self.__taxRates=set()
         with open(bracketFile,"r") as f:
           brackets=f.readlines()
         #splits indivdual brackets lines into seperate lists
         for lower,upper,taxRate in list(map(lambda x: x.split(","),brackets)):
                self.__taxRates.add((float(lower),float(upper),float(taxRate)))
            #converts each key value pair to their respective data type and adds them  to set as tuple
            
    #retrieves the marginal tax rate for a given income
    def getMarginalRate(self,taxableIncome):
        #comparing the upper element at index 1
        return min(filter(lambda e: taxableIncome<=e[1],self.__taxRates))[2]
        
    def computeTaxes(self,taxableIncome):
        applicableRates=filter(lambda e: taxableIncome>=e[1],self.__taxRates)
        #get rates that would apply to this income
        totalTaxes=0
        for lower,upper, rate in applicableRates:
            marginal=0
            if upper>taxableIncome:
                marginal=taxableIncome-lower
            else:
                marginal=upper-lower
            totalTaxes+=marginal*rate
        return totalTaxes