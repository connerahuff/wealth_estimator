
"""
Appreciating asset types include
-Savings
-checking
-stock
    -401k
    -espp
    -rsu
-home
-rental property

Depreciating assets include
-car

Forms of expenses
-monthly expenses
-rent
-car insurance
-vacations
-buying a new car


"""
class AssetType:

    def __init__(self, name, current_value):
        self.name = name
        self.current_value = current_value

class AppreciatingAsset(AssetType):

    def __init__(self, name, current_value, apy, expense_ratio, flat_monthly_fee):
        AssetType.__init__(self, name, current_value)
        self.apy = apy
        self.expense_ratio = expense_ratio
        self.flat_monthly_fee = flat_monthly_fee

    def advance_month(self):
        self.current_value += self.current_value * (self.apy/12)
        self.current_value -= self.current_value * (self.expense_ratio/12)
        self.current_value -= self.flat_monthly_fee

    def add_value_to_account(self, added_value):
        self.current_value += added_value