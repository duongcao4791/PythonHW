# ----------------------------------------------------------------------
# Name:        interestcal
# Purpose:     CS 122 Homework 2
#
# Author(s): Haitao Huang, Duong Cao
# ----------------------------------------------------------------------
"""
Compute and print the accrued amount after 10, 20, 30, 40 and 50 years.

Prompt the user for a proper principle amount.
Prompt the user for a proper interest rate.
Compute the accrued amounts.
Print the accrued amounts.
"""
max_principal = 1000000 # the maximum principal amount
max_rate = 20 # the maximum interest rate

def prompt_principal():
    """
    Repeatedly prompt the user for a valid principal amount
    :return: (number) the principal amount
    """
    valid = False
    while not valid:
      principal = float(input("Please enter principal amount: $"))
      if principal >= 0 and principal <= max_principal:
        valid = True
      else:
        print('Invalid amount. Principal must be between $0 and $1,000,000.')
    return principal

def prompt_rate():
    """
    Repeatedly prompt the user for a valid interest rate
    :return: (number) the interest rate
    """
    valid = False
    while not valid:
      rate = float(input("Please enter interest rate: %"))
      if rate >= 0 and rate <= max_rate:
        valid = True
      else:
        print('Invalid rate. Interest rate must be between 0% and 20%.')
    return rate

def accrued_amt(principal, rate):
    """
    Compute and print the accrued amounts
    :param principal: (number) the principal amount
    :param rate: (number) the interest rate
    :return: None
    """
    amt = principal
    converted_rate = rate / 100
    for years in range(10, 51, 10):
      for i in range(0, 10):
        amt = amt * (1 + converted_rate)
      formatted_amt = f'${amt:,.2f}'
      print(f'Accrued amount after {years} years: {formatted_amt:>20}')

def main():
    principal = prompt_principal()
    rate = prompt_rate()
    accrued_amt(principal, rate)

if __name__ == "__main__":
    main()
