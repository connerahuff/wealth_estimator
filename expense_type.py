
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

class Rent(ExpenseType):