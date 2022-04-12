April 11th 2022
Mitchell Culligan
Sfwrtech 3pr3 Final Project

For the final project I was tasked with using all the knowledge I have acquired throughout the semester to 
create a system that someone could use to file their taxes in Canada.

To accomplish this goal the program makes 
use of several text files to store and retrieve information regarding tax rates in canada as well as storing user information.
Multiple classes to repersent grouped information that I thought would be important in a Tax system. For example, the 
Account class to store very basic user data that is referenced in other classes with an associative relationship. One 
of the most important classes to the system is the TaxObject class which is the base class of an inheritance hierarchy.
Essentially my thought process behind creating this class was the need to couple a monetary value to a real world object within the scope of a tax system.
That object being described could be a deductable, student loan payment, capital gain, etc.  The Income class inherits from the TaxObject class as it shares
much of behavior as a TaxObject but has the additional functionality of partitioning some of its value to be taxed. Withdrawls from a RRSP account or 
gains acquired on a piece of capital recently sold this year would also be considered as a form of income in canada. It would be approriate for all these
different forms of income to inherit from the income class because they are all different incomes but they deserve their own classes because similar to the regular income
class they partition part of their value to be taxed however the different incomes would perform this functionality in different ways.
For thee RRSPWithdrawl class the amount of taxable income is dependent on the amount withdrawld throughout the year. These specific rates are acquired using the TaxBracket \
class.The TaxBracket class is used to store data upon tax rates as well as provide certain operations to be performed with those rates such as retrieving marginal 
rates or computing taxes based off of taxable income provided. The rates are retrieved from specific files provided  during the instanstiation of the object.
The TaxReturn class is used to generate a basic tax form for a given user. The user information is provided through an Account object and further information
about that user such as gross income and deductables throughout the year are acquired in different methods. Once all the needed information has been provided from the user
the class is able to create a new tax form and file it in the taxforms directory.

The flow of execution for the program is simple as the user is first asked to create a new account to be used. This is done by asking basic information about the user
such as their full name, last name, and sin number. Then once completed the user is prompted for specific information about their income and deductables throughout the year.
Once all information has been successfully entered a tax return form is generated as stated before with the TaxReturn class.
Once a new form has been written the user is then prompted if they would like to file another tax form, beginning the process over again, or they can choose to end the program.
Two modules are used as helpers and provide specific functions that assist in specific use cases related to input and output formatting.


