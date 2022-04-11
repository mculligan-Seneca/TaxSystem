

#this function ensures that the input provided by the user is a positive number 
def ensurePositiveFloat(value)->float:
    num=-1
    while num<0:
        collected=input(f'Enter value for {value}: ')
        if not collected.isnumeric() or (num:=float(collected))<0:
            print("Invalid input! Must be positive number")
        
    return num





#this function takes in input from the user and ensures it is a positive number
# input valsrepresents an list of variables to be inputed from the user
def getSpecifiedInput(inputVals):
    return list(map(ensurePositiveFloat,inputVals))
        