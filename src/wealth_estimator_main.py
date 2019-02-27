from asset_type import AppreciatingAsset
from time_simulator import TimeSim
from income_type import Salary
from finances import FinanceScenario
import matplotlib.pyplot as plt
from expense_type import AppreciatingExpense
from expense_type import ExpenseType
import config as cfg

def main():
    #first financial scenario
    income_list_1 = []
    income_list_1.append(Salary("Qualcomm Salary", 129500, 3, 19, 20))

    asset_list_1 = []
    asset_list_1.append(AppreciatingAsset("Vanguard S&P 500", 216000, 9.8,
                      0.3, 4, cfg.INFLATION_ADJ, 100))

    expense_list_1 = []
    expense_list_1.append(AppreciatingExpense("Conner's rent", 900, 5))
    expense_list_1.append(AppreciatingExpense("Conner's expenses", 1300,
                                            cfg.INFLATION_RATE))

    finances_1 = FinanceScenario(income_list_1, asset_list_1, expense_list_1)
    time_sim_1 = TimeSim(finances_1, 30)
    time_sim_1.start_sim()

    #second financial scenario
    income_list_2 = []
    income_list_2.append(Salary("Qualcomm Salary", 129500, 3, 19, 20))

    asset_list_2 = []
    asset_list_2.append(AppreciatingAsset("Vanguard S&P 500", 216000, 9.8,
                      0.3, 4, cfg.NON_INFLATION_ADJ, 100))

    expense_list_2 = []
    expense_list_2.append(AppreciatingExpense("Conner's rent", 900, 5))
    expense_list_2.append(AppreciatingExpense("Conner's expenses", 1300,
                                            cfg.INFLATION_RATE))

    finances_2 = FinanceScenario(income_list_2, asset_list_2, expense_list_2)
    time_sim_2 = TimeSim(finances_2, 30)
    time_sim_2.start_sim()

    #post process the collected data
    wealth_over_time_1 = sorted(time_sim_1.money_snapshot.items())
    x_1, y_1 = zip(*wealth_over_time_1)
    line_1 = plt.plot(x_1, y_1, label="Wealth adjusted for inflation")

    wealth_over_time_2 = sorted(time_sim_2.money_snapshot.items())
    x_2, y_2 = zip(*wealth_over_time_2)
    #newy2 = [x/1.03 for x in y2]
    line_2 = plt.plot(x_2, y_2, label="Wealth not adjusted for inflation")

    # Create a legend for the first line.
    first_legend = plt.legend(loc=2)
    plt.xlabel("Dollar amount")
    plt.ylabel("Years")

    # Add the legend manually to the current Axes.
    ax = plt.gca().add_artist(first_legend)

    plt.show()


if __name__ == "__main__":
    main()
