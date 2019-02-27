""" Container class for income, expenses, and assets """
from asset_type import AssetType
#from time_simulator import TimeSim
from income_type import Salary
from expense_type import AppreciatingExpense


class FinanceScenario():

    def __init__(self, income_list, asset_list, expense_list):
        self.income_list = income_list
        self.asset_list = asset_list
        self.expense_list = expense_list

    def total_asset_appraisal(self):
        total_asset_value = 0

        #loop through assets to figure out how much net worth is had
        for asset in self.asset_list:
            total_asset_value += asset.current_value
        return total_asset_value

    def calculate_revenue(self, months_advanced, new_year):
        earnings = 0

        for income in self.income_list:
            if type(income) is Salary:
                earnings += (income.net_income - income.espp_allotment)/12
                #rough 5.5k yearly match at 19k total, will increase with inftn
                earnings += ((income.retire_set_aside)/12) * 1.33
                if ((months_advanced + 1) % 6 == 0):
                    #get 15% discount on espp allotment
                    earnings += (income.espp_allotment/2)*1.15
                if new_year:
                    income.advance_year()
        return earnings

    def utilize_monthly_income(self, months_advanced):
        earnings = 0
        new_year = False

        if ((months_advanced + 1) % 12 == 0):
            new_year = True

        #TODO: handle non salary cases loop through income list to
        # divy up the earnings
        earnings = self.calculate_revenue(months_advanced, new_year)

        #set aside pretax income

        #TODO: implement expenses and subtract expenses from take home pay
        for expense in self.expense_list:
            is_rent = (type(expense) is AppreciatingExpense)
            print("Subtracting " + str(expense.monthly_expense) + " from " +
                  str(earnings) + " " + str(is_rent) + " \n")
            earnings -= expense.monthly_expense
            if new_year and type(expense) is AppreciatingExpense:
                expense.advance_year()
        #Add income to various asset accounts
        for asset in self.asset_list:
            asset.add_value_to_account(earnings *
                                       asset.earnings_deposit_pct/100)
            asset.advance_month()