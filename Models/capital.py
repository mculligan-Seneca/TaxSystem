from Models.income import Income


#Capital class repersents a relieaved capital gain to be tax
#for example the sale of an asset
class Capital(Income):

    def __init__(self,proceeds,adjustedCosts,expenses,description):
        Income.__init__(self,proceeds-(adjustedCosts+expenses),description)
  

    #tax calculation for relieaved capital is 1/2*value of capital * the marginal tax rate
    def getTaxableIncome(self):
        
        return 0.5*super().getAmount()

  