from Helpers.InputValidation import *
from Helpers.MenuHelper import *
from Models.income import Income
from Models.capital import *
from Models.account import Account
from Models.rrspwithdrawl import RRSPWithdrawl
from tabulate import tabulate
from Models.taxobject import TaxObject
from Models.taxbracket import TaxBracket
import numpy as np
class TaxReturn:

    def __init__(self,account:Account):
        self.__account=account
        self.__incomes=[]
        self.__deductables=[]
        self.__fedTax=TaxBracket("TaxRates/personal/personal_fed_tax_rates.txt")
        self.__provTax=TaxBracket(f'TaxRates/personal/province/personal_{self.__account.getProvince()}_tax_rates.txt')
        


      
        
                

    def __createPensionWithdrawl(self):
     print("Did you withdrawl from your pension?")
     pension=None
     select=displayMenu({1:"Yes",0:"No"})
     if select==1:
       withdrawlAmount=ensurePositiveFloat("Withdawl amount")
       pension=RRSPWithdrawl(withdrawlAmount,"RRSP Withdrawl",self.__account.getProvince()=="qc")
     return pension
     
    #requries the user to enter specifc information regarding their income this year
    def acquireGrossIncome(self):
        print("\nGather Gross Income\n")
        choice="N"
        while choice.lower()!='y':
            incomeList=[]
            incomeList.append(Income(ensurePositiveFloat("Employment Income"),"Employment Income"))
            incomeList+=generateList("Do you want to add unrelieaved capital gains?",createCapitalGains)
            incomeList+=[] if (pension:=self.__createPensionWithdrawl())is None else [pension]
            print("Income Evaluation")
            print("-"*10)
            table=formatTable(incomeList,["Type of Income", "Amount"],formatter=taxObjectFormatter)
            print(table)
            print()
            choice = input("Is this valid? (Y/y): ")
            
            

        self.__incomes=incomeList


    #requires user to input information about their deductions
    def acquireDeductions(self):
        print("\nGather Deductables\n")
        choice="N"
        while choice.lower()!='y':
            deductList=[]
            deductList+=[] if (interestAmount:=ensurePositiveFloat("Interest paid on loans"))==0 else [TaxObject(interestAmount,"Interest from loans")]
            deductList+=[] if (interestAmount:=ensurePositiveFloat("Student Tuition paid"))==0 else [TaxObject(interestAmount,"Student Tuition")]
            table=formatTable(deductList,["Type of Deduction", "Amount"],formatter=taxObjectFormatter)
            print(table)
            choice = input("Is this valid? (Y/y): ")
            
        self.__deductables=deductList
        

    def generateTaxForm(self):
        FILE_NAME="taxforms/Tax_Form_{fullName}.txt"
        taxReturn="Account:\n"+str(self.__account)
        taxReturn+=formatTable(self.__incomes,["Income","Amount","Taxable Amount"],formatter=taxableIncomeFormatter)+"\n\n"
        taxReturn+=formatTable(self.__deductables,["Deductables","Amount"],formatter=taxObjectFormatter)+"\n\n"
        taxableIncome=np.sum([x.getTaxableIncome() for x in self.__incomes])
        deductableAmount=np.sum([ x.getAmount() for x in self.__deductables])
        taxReturn+=f'Taxable Income before deductions: ${format(taxableIncome,",.2f")}\n'
        taxReturn+=f'Total deductions: ${format(deductableAmount,",.2f")}\n'
        taxableIncome-=deductableAmount

        fedRate=self.__fedTax.getMarginalRate(taxableIncome)
        provRate=self.__provTax.getMarginalRate(taxableIncome)
        taxReturn+="Federal Marginal Rate {:.0%}\nProvincial Marginal Rate {:.0%}\n".format(fedRate,provRate)
        fedTaxAmount=self.__fedTax.computeTaxes(taxableIncome)
        provTaxAmount=self.__provTax.computeTaxes(taxableIncome)
        taxReturn+="Federal Taxes: ${:,.2f}\nProvincial Taxes: ${:,.2f}\n".format(fedTaxAmount,provTaxAmount)
        taxReturn+="Total Taxes: ${:,.2f}\n".format(fedTaxAmount+provTaxAmount)
        print(taxReturn)
        input("Press any key to save tax return...")
        with open(FILE_NAME.format(fullName=self.__account.getFullName()),"w") as f:
            f.write(taxReturn)
        print("Tax Form successfully generated!")       


        




def createCapitalGains():
       
    capitalName=input("Enter the name of the capital: ")
    proceeds,adjustedCosts,expenses=getSpecifiedInput(["Profit","original price of capital ", "expenses"])

    return Capital(proceeds,adjustedCosts,expenses,capitalName)


                
