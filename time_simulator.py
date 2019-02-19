#main functions: advance time by a month
#call list of accounts open to advance by month
#output result data into JSON format to be interpretted by matlibplot

import datetime
import calendar
from finances import Finances

class TimeSim():
    def __init__(self, finances, years):
        self.start_time = datetime.date.today()
        self.current_time = self.start_time
        self.months_advanced = 0
        self.finances = finances
        self.total_months = years * 12
        self.money_snapshot = {}

    def advance_month(self, source_date, months):
        month = source_date.month - 1 + months
        year = source_date.year + month // 12
        month = month % 12 + 1
        day = min(source_date.day,calendar.monthrange(year,month)[1])
        self.months_advanced += 1
        return datetime.date(year,month,day)

    def start_sim(self):
        while (self.months_advanced <= self.total_months):
            #Add total value of each account into dictionary
            self.money_snapshot[self.months_advanced] = self.finances.total_asset_appraisal()
            self.finances.utilize_monthly_income(self.months_advanced)
            self.current_time = self.advance_month(self.current_time, 1)
        print("Finished time sim")
