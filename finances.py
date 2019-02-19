""" Container class for income, expenses, and assets """
from asset_type import AssetType
#from time_simulator import TimeSim
from income_type import Salary


class Finances():

    def __init__(self, income_list, asset_list, expense_list):
        self.income_list = income_list
        self.asset_list = asset_list
        self.expense_list = expense_list

    def advance_month(self):
        do = 0
        for income_source in self.income_list:
            if (type(income_source) == Salary):
                do = 1
        return do

    def total_asset_appraisal(self):
        total_asset_value = 0

        #loop through assets to figure out how much net worth is had
        for asset in self.asset_list:
            total_asset_value += asset.current_value
        return total_asset_value

    def utilize_monthly_income(self, months_advanced):
        espp_month = False
        new_year = False
        earnings = 0
        salary = None

        if ((months_advanced + 1) % 6 == 0):
            espp_month = True
        if ((months_advanced + 1) % 12 == 0):
            #update salary info
            for income in self.income_list:
                if type(income) is Salary:
                    new_year = True
                    salary = income

        #TODO: handle non salary cases loop through income list to divy up the earnings
        for income in self.income_list:
            if type(income) is Salary:
                earnings += (income.net_income - income.espp_allotment)/12
                earnings += ((income.retire_set_aside)/12) * 1.05
                if espp_month is True:
                    earnings += (income.espp_allotment/2)*1.15
        #TODO: implement expenses and subtract expenses from take home pay

        #Add income to various asset accounts
        for asset in self.asset_list:
            asset.add_value_to_account(earnings)
            asset.advance_month()
            break
        #update salary info for the next 12 months
        if new_year is True:
            salary.advance_year()