
""" Forms of expenses
-monthly expenses
-rent
-car insurance
-vacations
-buying a new car """

class ExpenseType():

    def __init__(self, name, monthly_expense):
        self.name = name
        self.monthly_expense = monthly_expense

class AppreciatingExpense(ExpenseType):

    def __init__(self, name, monthly_expense, yearly_inc_pct):
        ExpenseType.__init__(self, name, monthly_expense)
        self.yearly_inc_pct = yearly_inc_pct

    def advance_year(self):
        self.monthly_expense += (self.monthly_expense * self.yearly_inc_pct/100)