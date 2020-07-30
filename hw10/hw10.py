# ----------------------------------------------------------------------
# Name: hw10
# Purpose: Demonstrate the use of Pandas
#
# Author(s): Duong Cao, Haitao Huang
# ----------------------------------------------------------------------
"""
Single module includes eleven functions to answer questions
based on 2020 Fe Guide.csv file which contains Fuel Economy Data
downloaded from the EPA website.
"""

import pandas as pd


def q1(df):
    """
    Q1: How many cars are made by the division Audi?
    :param df: 2020 Fe Guide.csv Pandas DataFrame
    :return: integer - number of cars made by division Audi
    """
    return len(df.loc[df['Division'] == 'Audi'])


def q2(df):
    """
    Q2: How many divisions does the manufacturer General Motors have?
    :param df: 2020 Fe Guide.csv Pandas DataFrame
    :return: integer - number of 'Division'
    """
    return len(df.loc[df['Mfr Name'] == 'General Motors', 'Division'].unique())


def q3(df):
    """
    Q3: Which manufacturer makes the most guzzlers?
    (as indicated by the column 'Guzzler?')
    :param df: 2020 Fe Guide.csv Pandas DataFrame
    :return: String - manufacturer makes the most guzzlers
    """
    return df.loc[df['Guzzler?'] == 'G', 'Mfr Name'].mode().loc[0]


def q4(df):
    """
    Q4: What is the value of the highest combined Fuel Efficiency
    as given by "Comb FE (Guide) - Conventional Fuel"?
    :param df: 2020 Fe Guide.csv Pandas DataFrame
    :return: float - value of the highest combined Fuel Efficiency
    """
    return df["Comb FE (Guide) - Conventional Fuel"].max()


def q5(df):
    """
    Q5: Which division and car line has the lowest combined
    FE - Conventional Fuel?
    :param df: 2020 Fe Guide.csv Pandas DataFrame
    :return: tuple - tuple of strings (division, carline)
    """
    return df.loc[df["Comb FE (Guide) - Conventional Fuel"].idxmin(),
                  'Division'], \
           df["Comb FE (Guide) - Conventional Fuel"].idxmin()


def q6(df):
    """
    Q6: What is the average combined FE - Conventional Fuel among
    all wheel drives. Use 'Drive Desc'
    :param df: 2020 Fe Guide.csv Pandas DataFrame
    :return: float - average value combined FE - Conventional Fuel among
    all wheel drives?
    """
    return df.loc[df["Drive Desc"] == "All Wheel Drive",
                  "Comb FE (Guide) - Conventional Fuel"].mean()


def q7(df):
    """
    Q7: Which car line has the largest difference between Highway
    and City Fuel efficiency - Conventional Fuel?
    :param df: 2020 Fe Guide.csv Pandas DataFrame
    :return: string - car line has the largest difference between
    Highway and City Fuel efficiency - Conventional Fuel
    """
    highway = df['Hwy FE (Guide) - Conventional Fuel']
    city = df['City FE (Guide) - Conventional Fuel']
    dif = abs(highway - city)
    return dif.idxmax()


def q8(df):
    """
    Q8: What is the average annual fuel cost
    (Annual Fuel1 Cost - Conventional Fuel) of supercharged cars?
    :param df: 2020 Fe Guide.csv Pandas DataFrame
    :return: float - average annual fuel cost of supercharged cars
    """
    return df.loc[df["Air Aspiration Method Desc"] == "Supercharged",
                  "Annual Fuel1 Cost - Conventional Fuel"].mean()


def q9(df):
    """
    Q9: What SUV has the lowest annual fuel cost?
    :param df: 2020 Fe Guide.csv Pandas DataFrame
    :return: string - SUV carline
    """
    return df.loc[df["Carline Class Desc"].str.contains("SUV", na=False),
                  "Annual Fuel1 Cost - Conventional Fuel"].idxmin()


def q10(df):
    """
    Q10: What is the average annual fuel cost by car division?
    :param df: 2020 Fe Guide.csv Pandas DataFrame
    :return: Pandas series - average annual fuel cost by car division
    """
    return df.groupby("Division").mean()[
        'Annual Fuel1 Cost - Conventional Fuel']


def q11(df):
    """
    Q11: What criteria would you use to buy a car?
    My criteria:
    1. BMW or Audi Division
    2. SUV
    3. All Wheel Drive
    4. Turbocharged
    5. Lowest annual fuel cost
    :param df: 2020 Fe Guide.csv Pandas DataFrame
    :return: string - carline
    """
    return df.loc[((df['Division'] == 'BMW') |
                  (df['Division'] == 'Audi')) &
                  (df['Carline Class Desc'].str.contains('SUV', na=False)) &
                  (df['Drive Desc'] == 'All Wheel Drive') &
                  (df['Air Aspiration Method Desc'] == 'Turbocharged'),
                  "Annual Fuel1 Cost - Conventional Fuel"].idxmin()


def main():
    df_fe = pd.read_csv('2020 FE Guide.csv', index_col='Carline', usecols=range(1, 449))
    print(f'Q1: {q1(df_fe)}')
    print(f'Q2: {q2(df_fe)}')
    print(f'Q3: {q3(df_fe)}')
    print(f'Q4: {q4(df_fe)}')
    print(f'Q5: {q5(df_fe)}')
    print(f'Q6: {q6(df_fe)}')
    print(f'Q7: {q7(df_fe)}')
    print(f'Q8: {q8(df_fe)}')
    print(f'Q9: {q9(df_fe)}')
    print(f'Q10:{q10(df_fe)}\n')
    print(f'Q11: {q11(df_fe)}')


if __name__ == "__main__":
    main()
