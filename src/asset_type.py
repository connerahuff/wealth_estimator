
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

class AssetType():

    def __init__(self, name, current_value, inflation_adjusted,
                 earnings_deposit_pct):
        self.name = name
        self.current_value = current_value
        self.inflation_adjusted = inflation_adjusted
        self.earnings_deposit_pct = earnings_deposit_pct

class AppreciatingAsset(AssetType):

    def __init__(self, name, current_value, apy, expense_ratio,
        flat_monthly_fee, inflation_adjusted, earnings_deposit_pct):
        AssetType.__init__(self, name, current_value, inflation_adjusted,
                           earnings_deposit_pct)
        self.apy = apy
        self.expense_ratio = expense_ratio
        self.flat_monthly_fee = flat_monthly_fee


    def advance_month(self):
        self.current_value += self.current_value * (self.apy/(12*100))
        self.current_value -= self.current_value * (self.expense_ratio/(12*100))
        self.current_value -= self.flat_monthly_fee
        #assumes a 3% yearly inflation adjustment, split amongst 12 months
        if (self.inflation_adjusted == True):
            self.current_value = self.current_value / (1.0025)

    def add_value_to_account(self, added_value):
        self.current_value += added_value
