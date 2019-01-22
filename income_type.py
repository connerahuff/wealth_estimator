""" 
Forms of income
-salary
    -espp
    -401k
-yearly comps
    -bonus
    -stock grants
-rental property
"""
class IncomeType():

    def __init__(self, name, monthly_income):
        self.name = name
        self.monthly_income = monthly_income

class Salary(IncomeType):

    def __init__(self, name, monthly_income, yearly_increase, ):
        IncomeType.__init__(self, name, monthly_income)
