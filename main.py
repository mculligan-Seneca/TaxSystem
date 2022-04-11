import datetime as dt
from Helpers.MenuHelper import *
from Models.account import Account
import pandas as pd
from Models.taxreturn import TaxReturn
import re


def createAccount()->Account:
    print("\nCreate Account\n")
    provinces=("ab","bc","mb","nb","nl","ns","ns","nt","nu","on","pe","qc","sk","yt")
    firstName=input("Enter your first Name: ")
    lastName=input("Enter your last name: ")
    select=displayMenu(dict(pd.Series(provinces)))
    prov=provinces[select]
    while re.search(r'^[0-9]{9}$',(sin:=input("Enter your sin: ").replace("-","").strip())) is None:
        print("Invalid sin number: Format {#########)")
    
    return Account(firstName,lastName,prov,sin)
    


    





def main():
    print("-"*10,"SFWRTECH 3PR3 Tax System","-"*10)
    print(dt.datetime.now().strftime("%c"))
    select=1
    while select==1:
        account=createAccount()
        taxReturn = TaxReturn(account)
        taxReturn.acquireGrossIncome()
        taxReturn.acquireDeductions()
        taxReturn.generateTaxForm()
        print("File another Tax return?")
        select=int(displayMenu({1:"Yes",0:"No"}))
    
    print("Thank You, Have a wonderful Day!")


    
   
    


    
  




if __name__=="__main__":
    main()