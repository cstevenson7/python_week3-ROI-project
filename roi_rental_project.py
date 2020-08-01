# class Property():
#     def __init__(self,price,rating):
        # self.price = price
        # self.rating = rating

class Rental():
    #initialize the class and the constructed values
    def __init__(self, cost, incomes, expenses):
        self.cost = cost
        self.incomes = incomes
        self.expenses = expenses
        """
            Rental requires 3 positional arguments
            cost - the building purchase price - int expected
            income - monthly income of building - dictionary expected
            expenses - monthly expenses of building -  dictionary expected

        """
    # Method to display the monthly expense or the monthly income dictionaries
    def showDictionary(self, type):
        if type == 'income':
            if self.incomes == {}:
                print("\nYou have not added any income information")
            else:
                print(f"\nHere is what you have for the monthly {type}.")
                for key,value in self.incomes.items():
                    print(key,":",value)
        else:
            if self.expenses == {}:
                print("\nYou have not added any expense information")
            else:
                print(f"\nHere is what you have for the monthly {type}.")
                for key,value in self.expenses.items():
                    print(key,":",value)
    
    #Method to add monthly incomes
    def addIncome(self):      
        while True:
            print("\nIncome types are Rental, Laundry, Parking, or Other") 
            inc_name = input("Enter income type and enter quit when you are done: ")
            if inc_name.lower().strip() == "quit" or inc_name.lower().strip() == "q":
                break
            if inc_name.lower().strip() == 'rental' or inc_name.lower().strip() == 'laundry' or  inc_name.lower().strip() == 'parking' or  inc_name.lower().strip()  == 'other':     
                try:
                    inc_amount = int(input("Enter the amount per month: "))
                    self.incomes[inc_name.lower()] = inc_amount
                except ValueError:              
                    print("Sorry, no decimal places or commas. \n ")
                    continue
            else: 
                 print("\nSorry, that is not a vaild choice for income type, try again")
                 continue
   


    
    #Method to add monthly expenses
    def addExpense(self):         
        while True:
            print("\nExpense types are:")
            print("Mortgage, Capital Expenditures, Taxes, Insurance, Utilities, Vacancy, Home Owners Association") 
            print("Yard Service, Repairs, Property Management, Other")
            exp_name = input("\n Enter expense type and enter quit when you are done: ")
            if exp_name.lower().strip() == "quit" or exp_name.lower().strip() == "q":
                break
            if exp_name.lower().strip() == 'mortgage' or exp_name.lower().strip() == 'capital expenditures' or  exp_name.lower().strip() == 'taxes' or  exp_name.lower().strip()  == 'insurance' or  exp_name.lower().strip()  == 'utilities' or  exp_name.lower().strip()  == 'vacancy' or  exp_name.lower().strip()  == 'home owners associaition' or  exp_name.lower().strip()  == 'yard service' or  exp_name.lower().strip()  == 'repairs' or  exp_name.lower().strip()  == 'property management' or  exp_name.lower().strip()  == 'other':     
                try:
                    exp_amount = int(input("Enter the amount per month: "))
                    self.expenses[exp_name.lower()] = exp_amount
                except:              
                    print("\nSorry,no decimal places or commas. ")
                    continue
            else: 
                 print("\nSorry, that is not a vaild choice for expense type, try again.")
                 continue
    #Method to sum up Income 
    def sumIncome(self):
        total_income = 0
        for value in self.incomes.values():
            total_income += value
        return total_income

    # #Method to sum up Expenses
    def sumExpenses(self):
        total_expenses = 0
        for value in self.expenses.values():
            total_expenses += value
        return total_expenses

    def calculateCashFlow(self):
        #total_income = self.sumIncome()
        print(f"\nTotal monthly income = ${self.sumIncome():,}")
        #total_expenses = self.sumExpenses()
        print(f"Total monthly expenses = ${self.sumExpenses():,}")
        cash_flow = self.sumIncome() - self.sumExpenses()
        print(f"\nTotal Monthly Cash Flow = ${cash_flow:,}")
        return cash_flow

    def inputCheck(self, name =""):
        while True:
                try:
                    user_input = int(input("Enter the amount of your " + name + ": "))
                    break
                except ValueError:
                    print("\nPlease enter a whole number.") 
        return user_input 

    
    def calculateROI(self, monthly_cash_flow):
        print("\nJust about done! Now we need your cash expenditures")
        down_payment = self.inputCheck('down payment')
        closing = self.inputCheck('closing costs')
        rehab = self.inputCheck('rehab costs')
        other_costs = self.inputCheck(' other cash outlays')
        total_cash_exp = down_payment + closing + rehab + other_costs
        annual_cash_flow = monthly_cash_flow * 12
        roi = annual_cash_flow / total_cash_exp * 100        
        print (f" \nYour Cash on Cash ROI for this building is {roi} %")

    #Method for user check entries  and start again
    def checkDictionary(self, type):
        if type == 'income':
            while True:
                ck_income = input("Are your income entries correct? y/n : ")
                if ck_income.lower() == 'n':
                    self.clearCalculator()
                    print ("The calculator has been cleared, please start again")
                elif ck_income.lower() == 'y':
                    break
                else:
                    print("Sorry, no a valid option, try again")
        else:
            while True:
                ck_exp = input("Are your expense entries correct? y/n : ")
                if ck_exp.lower() == 'n':
                    self.clearCalculator()
                    print("The calculator has been cleared, please start again")
                elif ck_exp.lower() == 'y':
                    break
                else:
                    print("Sorry, no a valid option, try again")

    
    # Method to clear calculator
    def clearCalculator(self):
        self.cost = 0
        self.incomes.clear()
        self.expenses.clear()    




def run():
    #creating building object which is an instance of the Rental class
    building = Rental(0,{},{})
 
    print("\nWelcome to the Cash on Cash Return on Investment Calculator!")
    print( "This calculator uses the Four Square Method. Please round numbers to nearest dollar.\nDisclaimer: use at own risk")
           
    #Add Monthly Income
    print("\nFirst you will enter the monthly income of your building:")                
    building.addIncome()
    building.showDictionary('income')
    building.checkDictionary('income')

    #Add Monthly Expenses
    print("\nNext you will enter the monthly expenses of your building:")                
    building.addExpense()
    building.showDictionary('expense')
    # clear_req = input("\n Do you want to clear the calculator and start again?  Enter yes or no: ")
    # if clear_req.lower() == "yes":
    #     building.clearCalculator()

    # Calculate Cash Flow and ROI
    building.calculateROI(building.calculateCashFlow())
    building.clearCalculator()


run()
            
                
    