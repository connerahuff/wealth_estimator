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

    def __init__(self, name, yearly_income):
        self.name = name
        self.yearly_income = yearly_income

class Salary(IncomeType):

    def __init__(self, name, yearly_income, yearly_increase, retire_pct, espp_pct):
        IncomeType.__init__(self, name, yearly_income)
        self.yearly_increase = yearly_increase
        self.retire_pct = retire_pct
        self.espp_pct = espp_pct
        self.retire_set_aside = self.set_aside_pretax_income()
        self.net_income = self.tax_salary()
        self.espp_allotment = self.set_aside_espp_amt()

    def set_aside_pretax_income(self):
        if (self.yearly_income * (self.retire_pct/100) > self.yearly_income):
            print("Yearly income, not high enough for retirement contribution")
            return 0
        else:
            return self.yearly_income * (self.retire_pct/100)

    def set_aside_espp_amt(self):
        espp_amt = 0
        if (self.net_income * (self.espp_pct/100) >= 10625):
            espp_amt = 10625
        else:
            espp_amt = self.net_income * (self.espp_pct/100)

        if (self.net_income - espp_amt < 0):
            print("ESPP amount is too high for net income")
            return 0
        return espp_amt

    def advance_year(self):
        self.yearly_income += self.yearly_income * (self.yearly_increase/100)
        self.retire_set_aside = self.set_aside_pretax_income()
        self.net_income = self.tax_salary()
        self.espp_allotment = self.set_aside_espp_amt()

    def tax_salary(self):
        effective_tax_rate = 0
        #uses effective tax rates assuming 92007 zip code
        if (self.yearly_income >= 10000000):
            effective_tax_rate = 52.07
        elif (self.yearly_income >= 5000000):
            effective_tax_rate = 51.49
        elif (self.yearly_income >= 2000000):
            effective_tax_rate = 49.75
        elif (self.yearly_income >= 1000000):
            effective_tax_rate = 46.86
        elif (self.yearly_income >= 800000):
            effective_tax_rate = 45.66
        elif (self.yearly_income >= 500000):
            effective_tax_rate = 42.27
        elif (self.yearly_income >= 400000):
            effective_tax_rate = 40.68
        elif (self.yearly_income >= 300000):
            effective_tax_rate = 38.18
        elif (self.yearly_income >= 250000):
            effective_tax_rate = 36.45
        elif (self.yearly_income >= 200000):
            effective_tax_rate = 34.08
        elif (self.yearly_income >= 150000):
            effective_tax_rate = 32.23
        elif (self.yearly_income >= 125000):
            effective_tax_rate = 31.55
        elif (self.yearly_income >= 100000):
            effective_tax_rate = 29.20
        elif (self.yearly_income >= 80000):
            effective_tax_rate = 26.63
        elif (self.yearly_income >= 70000):
            effective_tax_rate = 24.87
        elif (self.yearly_income >= 55000):
            effective_tax_rate = 21.16
        elif (self.yearly_income >= 45000):
            effective_tax_rate = 18.93
        elif (self.yearly_income >= 30000):
            effective_tax_rate = 15.99
        elif (self.yearly_income >= 20000):
            effective_tax_rate = 12.78
        elif (self.yearly_income >= 10000):
            effective_tax_rate = 8.21
        else:
            effective_tax_rate = 7.77

        return self.yearly_income - (self.yearly_income * (effective_tax_rate/100))

    
        