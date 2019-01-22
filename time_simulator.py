#main functions: advance time by a month
#call list of accounts open to advance by month
#output result data into JSON format to be interpretted by matlibplot

import datetime
import calendar

class TimeSim:

    def __init__(self, income_list, asset_list, expense_list, years):
        self.start_time = datetime.date.today()
        self.current_time = self.start_time
        self.months_advanced = 0
        self.income_list = income_list
        self.asset_list = asset_list
        self.expense_list = expense_list
        self.total_months = years * 12

    def advance_month(self, source_date, months):
        month = source_date.month - 1 + months
        year = source_date.year + month // 12
        month = month % 12 + 1
        day = min(source_date.day,calendar.monthrange(year,month)[1])
        self.months_advanced += 1
        return datetime.date(year,month,day)

    def calculate_change(self):
        #loop through income list to divy up the earnings

        #subtract expenses from take home pay

        #Add income to various asset accounts
        do_nothing = 0

    def start_sim(self):
        while (self.months_advanced <= self.total_months):
            self.calculate_change()
            #Add total value of each account into dictionary
            
            self.current_time = self.advance_month(self.current_time, 1)
            self.months_advanced += 1

income = []
assets = []
expenses = []
time = TimeSim()
time.start_sim()
#time.start_time.tm_year = time.start_time.tm_year + 1
print(time.start_time)