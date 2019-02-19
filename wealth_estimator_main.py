from asset_type import AppreciatingAsset
from time_simulator import TimeSim
from income_type import Salary
from finances import Finances
import matplotlib.pyplot as plt

def main():

    income_list = []
    #129500
    income_list.append(Salary("Qualcomm Salary", 185500, 3, 19, 20))
    asset_list = []
    asset_list.append(AppreciatingAsset("Vanguard S&P 500", 216000, 9.8,
                      0.3, 4, True))
    expense_list = []
    finances = Finances(income_list, asset_list, expense_list)
    time_sim = TimeSim(finances, 30)
    time_sim.start_sim()

    wealth_over_time = sorted(time_sim.money_snapshot.items())
    x, y = zip(*wealth_over_time)
    line_1 = plt.plot(x, y, label="Wealth")

    """ 
    x2, y2 = zip(*wealth_over_time)
    newy2 = [x/1.03 for x in y2]
    line_2 = plt.plot(x2, newy2, label="Wealth adjusted for inflation")
    """

    # Create a legend for the first line.
    first_legend = plt.legend(loc=2)

    # Add the legend manually to the current Axes.
    ax = plt.gca().add_artist(first_legend)

    plt.show()


if __name__ == "__main__":
    main()
