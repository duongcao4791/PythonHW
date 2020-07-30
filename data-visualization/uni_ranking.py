# ----------------------------------------------------------------------
# Name:        Top 30 World University Ranking 2020
# Purpose:     Demonstrate the functionality of matplotlib
#
# Author:      Duong Cao
# ----------------------------------------------------------------------
"""
Implement a program that get the World University Ranking 2020 dataset
and use the matplotlib to explore it
"""
import pandas as pd
import matplotlib.pyplot as plt


def explore_ranking():
    """
    Use matplotlib to explore the World_University_Rank_2020 dataset
    """
    # Read the pypl csv file and don't use the index
    df = pd.read_csv('World_University_Rank_2020.csv', index_col=False)
    # Take only top 30 university from the dataset
    top_30 = df.loc[df['Rank'] <= 30]
    # Group top 30 university by Country
    group = top_30.groupby('Country', sort=False)['University'].count()
    # import the data to matplotlib pie
    plt.pie(group, explode=(0, 0.1, 0, 0, 0, 0, 0, 0),
            autopct=make_autopct(group))
    plt.title('Top 30 World University Ranking 2020 by Country')
    plt.legend(title='Country', loc='center left',
               labels=group.index, bbox_to_anchor=(1, 0, 0.5, 1))
    plt.show()
    print(type(group))


def make_autopct(values):
    """
    Function to show the percentage and value of autopct
    :param values: the panda series values
    :return: (list of tuple) countries and their number of university
    """
    def my_autopct(pct):
        """
        Child function to take the percentage of the values
        :param pct:
        :return: (float) and (integer) percentage and number of universities
        """
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{p:.0f}%''({v:d})'.format(p=pct, v=val)

    return my_autopct


def main():
    explore_ranking()


if __name__ == '__main__':
    main()
