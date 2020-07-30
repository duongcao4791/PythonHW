# # ----------------------------------------------------------------------
# # Name:        hw10
# # Purpose:     Demonstrate the use of Pandas
# #
# # Author:      Duong Cao, Haitao Huang
# # ----------------------------------------------------------------------
# """
# Load the relevant data into a Pandas data frame and answer the following
# questions:
#
# 1.How many cars are made by the division Audi?
# 2.How many divisions does the manufacturer General Motors have?
# 3.Which manufacturer makes the most guzzlers?
# 4.What is the value of the highest combined Fuel Efficiency?
# 5.Which division and car line has the lowest combined FE - Conventional
# Fuel?
# 6.What is the average combined FE - Conventional Fuel among all wheel
# drives?
# 7.Which car line has the largest difference between Highway and City
# Fuel efficiency - Conventional Fuel?
# 8.What is the average annual fuel cost (Annual Fuel1 Cost - Conventional
# Fuel) of supercharged cars?
# 9.What SUV has the lowest annual fuel cost?
# 10.What is the average annual fuel cost by car division?
# 11.What criteria would you use to buy a car?
# """
# import pandas as pd
#
#
# def q1(df):
#     """
#     How many cars are made by the division Audi?
#     :param df: Pandas DataFrame representing the data in
#                '2020 FE Guide.csv'
#     :return: integer
#     """
#     return len(df.loc[df['Division'] == 'Audi'])
#
#
# def q2(df):
#     """
#     How many divisions does the manufacturer General Motors have?
#     :param df: Pandas DataFrame representing the data in
#                '2020 FE Guide.csv'
#     :return: integer
#     """
#     return len(df.loc[df['Mfr Name'] == 'General Motors', 'Division'].unique())
#
#
# def q3(df):
#     """
#     Which manufacturer makes the most guzzlers?
#     :param df: Pandas DataFrame representing the data in
#                '2020 FE Guide.csv'
#     :return: string
#     """
#     # df_guzzlers = df.loc[df['Guzzler?']=='G']
#     # return df_guzzlers['Mfr Name'].mode().loc[0]
#     return df.loc[df['Guzzler?'] == 'G', 'Mfr Name'].mode().loc[0]
#
#
# def q4(df):
#     """
#     What is the value of the highest combined Fuel Efficiency?
#     :param df: Pandas DataFrame representing the data in
#                '2020 FE Guide.csv'
#     :return: float
#     """
#     return df['Comb FE (Guide) - Conventional Fuel'].max()
#
#
# def q5(df):
#     """
#     Which division and car line has the lowest combined FE -
#     Conventional Fuel?
#     :param df: Pandas DataFrame representing the data in
#                '2020 FE Guide.csv'
#     :return: tuple (string, string) division and car line
#     """
#     lowest_combined_FE = df['Comb FE (Guide) - Conventional Fuel'].idxmin()
#     return df.loc[lowest_combined_FE, 'Division'], lowest_combined_FE
#
#
# def q6(df):
#     """
#     What is the average combined FE - Conventional Fuel among all wheel
#     drives?
#     :param df: Pandas DataFrame representing the data in
#                '2020 FE Guide.csv'
#     :return: float
#     """
#     return df.loc[df['Drive Desc'] == 'All Wheel Drive',
#                   'Comb FE (Guide) - Conventional Fuel'].mean()
#
#
# def q7(df):
#     """
#     Which car line has the largest difference between Highway and City
#     Fuel efficiency - Conventional Fuel?
#     :param df: Pandas DataFrame representing the data in
#                '2020 FE Guide.csv'
#     :return: string
#     """
#     return abs(df['Hwy FE (Guide) - Conventional Fuel'] -
#                df['City FE (Guide) - Conventional Fuel']).idxmax()
#
#
# def q8(df):
#     """
#     What is the average annual fuel cost (Annual Fuel1 Cost -
#     Conventional Fuel) of supercharged cars?
#     :param df: Pandas DataFrame representing the data in
#                '2020 FE Guide.csv'
#     :return: float
#     """
#     return df.loc[df['Air Aspiration Method Desc'] == 'Supercharged',
#                   'Annual Fuel1 Cost - Conventional Fuel'].mean()
#
#
# def q9(df):
#     """
#     What SUV has the lowest annual fuel cost?
#     :param df: Pandas DataFrame representing the data in
#                '2020 FE Guide.csv'
#     :return: string - carline
#     """
#     return df.loc[df['Carline Class Desc'].str.contains('SUV', na=False),
#                   'Annual Fuel1 Cost - Conventional Fuel'].idxmin()
#
#
# def q10(df):
#     """
#     What is the average annual fuel cost by car division?
#     :param df: Pandas DataFrame representing the data in
#                '2020 FE Guide.csv'
#     :return: Pandas Series containing the division and avg annual fuel
#     """
#     return df.groupby('Division').mean()[
#         'Annual Fuel1 Cost - Conventional Fuel']
#
#
# def q11_duong(df):
#     """
#     Duong's perfect car.
#     Criteria:
#     1. BMW or Audi Division
#     2. SUV
#     3. All Wheel Drive
#     4. Turbocharged
#     5. Lowest annual fuel cost
#     :param df: 2020 Fe Guide.csv Pandas DataFrame
#     :return: string - carline
#     """
#     return df.loc[((df['Division'] == 'BMW') |
#                    (df['Division'] == 'Audi')) &
#                   (df['Carline Class Desc'].str.contains('SUV', na=False)) &
#                   (df['Drive Desc'] == 'All Wheel Drive') &
#                   (df['Air Aspiration Method Desc'] == 'Turbocharged'),
#                   "Annual Fuel1 Cost - Conventional Fuel"].idxmin()
#
#
# def q11_haitao(df):
#     """
#     Haitao's perfect car.
#     Criteria:
#     1.Made by manufacture Ferrari or Porsche
#     2.Auto transmission
#     3.All Wheel Drive
#     4.Highest combined Fuel Efficiency
#     :param df: Pandas DataFrame representing the data in
#                '2020 FE Guide.csv'
#     :return: string - carline
#     """
#     return df.loc[((df['Mfr Name'] == 'Ferrari') | (df['Mfr Name'] == 'Porsche') &
#                    (df['Transmission'].str.contains('Auto')) &
#                    (df['Drive Desc'] == 'All Wheel Drive')),
#                   'Comb FE (Guide) - Conventional Fuel'].idxmax()
#
#
# def main():
#     df_cars = pd.read_csv('2020 FE Guide.csv', index_col='Carline',
#                           usecols=lambda column: column not in ['Model Year'])
#     print(f'Q1: {q1(df_cars)}')  # 39
#     print(f'Q2: {q2(df_cars)}')  # 4
#     print(f'Q3: {q3(df_cars)}')  # Volkswagen Group of
#     print(f'Q4: {q4(df_cars)}')  # 58.0
#     print(f'Q5: {q5(df_cars)}')  # ('Bugatti', 'Chiron')
#     print(f'Q6: {q6(df_cars)}')  # 22.226256983240223
#     print(f'Q7: {q7(df_cars)}')  # CORVETTE
#     print(f'Q8: {q8(df_cars)}')  # 2791.4634146341464
#     print(f'Q9: {q9(df_cars)}')  # ESCAPE FWD HEV
#     print(f'Q10: {q10(df_cars)}')
#     print('Q11:')
#     print(f'Duong\'s perfect car: {q11_duong(df_cars)}')
#     print(f'Haitao\'s perfect car: {q11_haitao(df_cars)}')
#
#
# if __name__ == "__main__":
#     main()
