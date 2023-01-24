class ROI:

    def __init__(self):
        self.name = None
        self.expense = 0
        self.revenue = 0
        self.investment = 0
        self.r_o_i = 0
        self.d_exp = {}
        self.d_rev = {}
    
    def calculator(self):
        cash_flow = int(self.revenue) - int(self.expense)
        Roi = int(cash_flow)*12 / int(self.investment)
        self.r_o_i = Roi
        print(f" Your Roi for you property is {Roi * 100}% ")

    def user_input(self):
        print("Hello, Welcome to the ROI calculator.Let's get started.")
        self.name = input("Can i have your good name: ")
        self.revenue = int(input("What was your total revenue: "))
        self.expense = int(input("What was your total expense: "))
        self.investment = int(input("What was your intital total investment: "))
        cash_flow = int(self.revenue) - int(self.expense)
        Roi = int(cash_flow) / int(self.investment)
        self.r_o_i = Roi
        print(f" Your Roi for you property is {float(Roi * 100)}% ")

    def edit_expense(self):
    
        while True:
            response = input("Would you like to add or remove? Enter 'a' to add, 'd' to remove, 'q' to quit: " )
            if response.lower() == 'a':
                x = str(input("What is the expense you want to add?"))
                z = int(input(f"How much is the cost of the {x}: "))
                self.d_exp[x] = z
                self.expense += sum(self.d_exp.values())
                
            elif response.lower() == 'd':
                x = str(input("What is the expense you want to delete? "))
                self.expense -= self.d_exp[x]
                del self.d_exp[x]
            elif response.lower() == 'q':
                break
            else:
                print("invalid input. Please try again.")
                
                
    def edit_revenue(self):
    
        while True:
            response = input("Would you like to add or remove? Enter 'a' to add, 'd' to remove, 'q' to quit : " )
            if response.lower() == 'a':
                x = str(input("What is the revenue you want to add?"))
                z = int(input(f"How much is the cost of the {x}: "))
                self.d_rev[x] = z
                self.revenue += sum(self.d_rev.values())
            elif response.lower() == 'd':
                x = str(input("What is the revenue you want to delete? "))
                self.revenue -= self.d_rev[x]
                del self.d_rev[x]
            elif response.lower() == 'q':
                break
            else:
                 print("invalid input. Please try again.")   

    #displays the Summary of the ROI
    
    def display(self):

        
        # expense = [self.expense]
        # revenue = [self.revenue]

        # for i in self.d_exp.values():
        #     expense.append(i)
        # for i in self.d_rev.values():
        #     revenue.append(i)

        print(f"Name: {self.name} ")
        print(f"Your total Expense: {self.expense}")
        print(f"Your total Revenue: {self.revenue}")
        cash_flow = int(self.revenue) - int(self.expense)
        Roi = int(cash_flow)*12 / int(self.investment)
        print(f"Your ROI: {float(self.r_o_i*100)}%")

class Main:
    def run():
        roi_run = ROI()

        while True:
            print("\nWelcome to ROI Calculator\n")
           
            print("""
Please choose from the options below:

[1] Calculate ROI
[2] Display ROI
[3] Edit Expenses
[4] Edit Revenue
[5] Exit 

""")

            response = input("Please pick a number for youre options: ")
            if response == '1':
                roi_run.user_input()
            elif response == '2':
                roi_run.display()
            elif response == '3':
                roi_run.edit_expense()
            elif response == '4':
                roi_run.edit_revenue()
            elif response == '5':
                break
            else:
                print("Invalid input. PLease Try Again.")


Main.run()
# i wanted to implement this nested dict in my main program so that it could take multiple users and save various types of expenses and revnues(AND be able to edit it).
# but I just ran out of time for it. Although i am going work on it this weekend.
#create a list of dictionaries that stores each user's expenses, revenues, Cash-flow, Initial Investment and ROI 

# users = {
#     'user' : [{
#         'expense': {
#                 'taxes': 500,
#                 'mortgage':1200,
#                 'insurance': 400
#         },
#         'revenue':{
#                 'rent': 2500,
#                 'cleaning': 500
#         },
#     'initial_investment': 200000,
#     'Roi': 0 
        
#     }]
# }


# print(users['user'][0]['expense']['taxes'])