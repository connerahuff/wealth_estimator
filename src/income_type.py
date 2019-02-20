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
import config as cfg

class IncomeType():

    def __init__(self, name, yearly_income):
        self.name = name
        self.yearly_income = yearly_income

class Salary(IncomeType):

    retirement_401k_limit = 19000
    espp_limit = 16500
    #value which increases every year by the inflation rate
    #we use this so that we dont have to store all the tax values individually
    inflation_factor = 1

    def __init__(self, name, yearly_income, yearly_increase, retire_pct,
                 espp_pct):
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
        elif (self.yearly_income * (self.retire_pct/100) >
              self.retirement_401k_limit):
            return self.retirement_401k_limit
        else:
            return self.yearly_income * (self.retire_pct/100)

    def set_aside_espp_amt(self):
        espp_amt = 0
        if ((self.net_income) * (self.espp_pct/100) >= self.espp_limit):
            espp_amt = self.espp_limit
        else:
            espp_amt = (self.net_income) * (self.espp_pct/100)

        if (self.net_income - espp_amt < 0):
            print("ESPP amount is too high for net income")
            return 0
        
        #since employees are given a 15% discount
        return espp_amt

    def adjust_for_inflation(self):
        self.retirement_401k_limit += (self.retirement_401k_limit *
                                       cfg.INFLATION_RATE / 100)
        self.espp_limit += self.espp_limit * cfg.INFLATION_RATE / 100
        self.inflation_factor = self.inflation_factor * cfg.INFLATION_RATE/100

    #this function updates in salary in the rear since we start
    # the sim at time 0
    def advance_year(self):
        self.yearly_income += self.yearly_income * (self.yearly_increase/100)
        self.retire_set_aside = self.set_aside_pretax_income()
        self.net_income = self.tax_salary()
        self.espp_allotment = self.set_aside_espp_amt()
        self.adjust_for_inflation()

    def tax_salary(self):
        effective_tax_rate = 0
        post_retire_income = self.yearly_income - self.retire_set_aside
        #uses effective tax rates assuming 92007 zip code
        if (post_retire_income >= 10000000 * self.inflation_factor):
            effective_tax_rate = 52.07
        elif (post_retire_income >= 5000000 * self.inflation_factor):
            effective_tax_rate = 51.49
        elif (post_retire_income >= 2000000 * self.inflation_factor):
            effective_tax_rate = 49.75
        elif (post_retire_income >= 1000000 * self.inflation_factor):
            effective_tax_rate = 46.86
        elif (post_retire_income >= 800000 * self.inflation_factor):
            effective_tax_rate = 45.66
        elif (post_retire_income >= 500000 * self.inflation_factor):
            effective_tax_rate = 42.27
        elif (post_retire_income >= 400000 * self.inflation_factor):
            effective_tax_rate = 40.68
        elif (post_retire_income >= 300000 * self.inflation_factor):
            effective_tax_rate = 38.18
        elif (post_retire_income >= 250000 * self.inflation_factor):
            effective_tax_rate = 36.45
        elif (post_retire_income >= 200000 * self.inflation_factor):
            effective_tax_rate = 34.08
        elif (post_retire_income >= 150000 * self.inflation_factor):
            effective_tax_rate = 32.23
        elif (post_retire_income >= 125000 * self.inflation_factor):
            effective_tax_rate = 31.55
        elif (post_retire_income >= 100000 * self.inflation_factor):
            effective_tax_rate = 29.20
        elif (post_retire_income >= 80000 * self.inflation_factor):
            effective_tax_rate = 26.63
        elif (post_retire_income >= 70000 * self.inflation_factor):
            effective_tax_rate = 24.87
        elif (post_retire_income >= 55000 * self.inflation_factor):
            effective_tax_rate = 21.16
        elif (post_retire_income >= 45000 * self.inflation_factor):
            effective_tax_rate = 18.93
        elif (post_retire_income >= 30000 * self.inflation_factor):
            effective_tax_rate = 15.99
        elif (post_retire_income >= 20000 * self.inflation_factor):
            effective_tax_rate = 12.78
        elif (post_retire_income >= 10000 * self.inflation_factor):
            effective_tax_rate = 8.21
        else:
            effective_tax_rate = 7.77

        return (post_retire_income -
                (post_retire_income * (effective_tax_rate/100)))

    
        