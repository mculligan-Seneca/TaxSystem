from Models.income import Income
from Models.account import Account
from Models.taxbracket import TaxBracket

class RRSPWithdrawl(Income):

    
    #isQuebec selects what taxbracket to use
    def __init__(self,withdrawlAmount, description,isQuebec=False):
        
        Income.__init__(self,withdrawlAmount,description)
        fileName="TaxRates/RRSP_withdrawl"
        if isQuebec:
            fileName+="/rrsp_qc_rates.txt"
        else:
            fileName+="/rrsp_fed_rates.txt"
        self.__bracket=TaxBracket(fileName)#get rates for withdrawl
        


    
    def getTaxableIncome(self):
        return super().getAmount()*self.__bracket.getMarginalRate(super().getAmount())

