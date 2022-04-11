from tabulate import tabulate

from Models.income import Income
from Models.taxobject import TaxObject



def displayMenu(optionsDict: dict,formatter=str):

    
    exit=False
    while not exit:
        print("Select an option: ")
        for k,v in optionsDict.items():
            print(f'{k} : {formatter(v)} ')
        selection=input(">: ")
        if not selection.isnumeric() or (selection:=int(selection)) not in optionsDict.keys():
            print("Invalid Input select an option above!")
        else:
            exit=True
    
    return selection


def formatTable(list,headers,formatter):
    formattedList=[formatter(obj) for obj in list]
    table=tabulate(formattedList,headers=headers)
    return table

def taxObjectFormatter(incomeObj:TaxObject):
    return [incomeObj.getDescription(),incomeObj.getAmount()]

def taxableIncomeFormatter(incomeObj: Income):
    return [incomeObj.getDescription(),incomeObj.getAmount(),incomeObj.getTaxableIncome()]

#this function builds a list of specific objects
def generateList(message,onGenerate):
     select=1
     list=[]
     while select==1:
           
      print(message)
      select=displayMenu({1:"Yes",0:"No"})
      if select==1:
          list.append(onGenerate())

           
     return list   