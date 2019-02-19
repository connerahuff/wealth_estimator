from asset_type import AppreciatingAsset
import matplotlib.pyplot as plt

total_years = 10

def define_investments():
    global asset_1
    global asset_2

    #14.39
    asset_1 = AppreciatingAsset("Vanguard 500 IDX", 75000, 9, 0.012, 3.75)
    asset_2 = AppreciatingAsset("Vanguard EXP ADM", 75000, 10.73, .32, 3.75)

if __name__ == "__main__":
    define_investments()
    asset_1_dict = {}
    asset_2_dict = {}
    for i in range(total_years):
        asset_1_dict[i] = asset_1.current_value
        asset_2_dict[i] = asset_2.current_value
        
        for j in range(12):
            asset_1.advance_month()
            asset_2.advance_month()
            asset_1.add_value_to_account(2042)
            asset_2.add_value_to_account(2042)

    list_1 = sorted(asset_1_dict.items())
    x1, y1 = zip(*list_1)
    line_1 = plt.plot(x1, y1, label=asset_1.name)

    list_2 = sorted(asset_2_dict.items())
    x2, y2 = zip(*list_2)
    line_2 = plt.plot(x2, y2, label=asset_2.name)

    # Create a legend for the first line.
    first_legend = plt.legend(loc=2)

    # Add the legend manually to the current Axes.
    ax = plt.gca().add_artist(first_legend)

    plt.show()