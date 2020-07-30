# ----------------------------------------------------------------------
# Name:        COVID19
# Purpose:     Practice crawling web pages with beautiful soup, re, and
#              urllib
#
# Author(s):   Haitao Huang, Duong Cao
# ----------------------------------------------------------------------
"""
Implement a program that systematically compiles COVID-19 information
from multiple web pages and saves that information in a text file on the
user's computer.
"""

import urllib.request
import urllib.parse
import bs4
import re


def visit_url(url):
    """
    Open the given url and return its visible content and the referenced
    links
    :param url:(string) - the address of the web page to be read
    :return: BeautifulSoup object
    """
    try:
        with urllib.request.urlopen(url) as url_file:
            bytes = url_file.read()
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {url}\n{url_err}')
    else:
        soup = bs4.BeautifulSoup(bytes, 'html.parser')
        return soup


def get_population(search):
    """
    Finding the population numbers of searched countries.
    :param search: (String) the search term
    :return: (list of tuples) countries and population numbers
    """
    URL = ('https://en.wikipedia.org/wiki'
           + '/List_of_countries_and_dependencies_by_population')
    soup = visit_url(URL)
    tables = soup.find_all('table')
    table = tables[0]
    result = []

    regex = re.compile(search, re.IGNORECASE)
    searched_countries = table.find_all('a', string=regex)
    for each_country in searched_countries:
        country = each_country.get_text()
        population = each_country.find_next('td').get_text()
        population = int(population.replace(',', ''))
        result.append((country, population))
    return result


def get_case(search):
    """
    Finding the cases and deaths due to COVID-19 of the searched
    countries
    :param search: (String) the search term
    :return: (list of tuple) countries and their number of COVID-19
             cases, deaths, and the description
    """
    URL = ('https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_'
           + 'pandemic_by_country_and_territory')
    soup = visit_url(URL)
    base_url = 'https://en.wikipedia.org/'
    table = soup.find('table', {'id': "thetable"})
    result = []

    regex = re.compile(search, re.IGNORECASE)
    non_empty_regex = re.compile(r'((/S )+(,|.))')
    searched_countries = table.find_all('a', string=regex)
    for each_country in searched_countries:
        country = each_country.get_text()
        next_td = each_country.find_next('td')
        try:
            cases = int(next_td.get_text().replace(',', ''))
        except ValueError:
            return result
        else:
            try:
                deaths = int(next_td.find_next('td').get_text()
                             .replace(',', ''))
            except ValueError:
                return result
            else:
                country_url = each_country.get('href')
                soup2 = visit_url(f'{base_url}{country_url}')
                paragraph = soup2.find('p')
                paragraph_text = paragraph.get_text()
                while not paragraph_text.strip():
                    paragraph = paragraph.find_next('p')
                    paragraph_text = paragraph.get_text()
                    if ',' and '.' not in paragraph_text:
                        paragraph_text = ''
                result.append((country, cases, deaths, paragraph.get_text()))
    return result


def main():
    search_term = input('Please enter a search term: ')
    pop = dict(get_population(search_term))
    cases = get_case(search_term)

    # write output
    with open(f'{search_term}summary.txt', 'w', encoding='utf-8') \
            as output_file:
        for i in range(len(pop)):
            country = cases[i][0]
            population = pop[country]
            confirms = cases[i][1]
            deaths = cases[i][2]
            paragraph = cases[i][3]
            cases_per_100k = f'{100000*confirms/population:,.1f}'
            deaths_per_100k = f'{100000*deaths/population:,.1f}'
            population = f'{population:,}'
            confirms = f'{confirms:,}'
            deaths = f'{deaths:,}'

            output_file.write(f'Country: {country} \n')
            output_file.write(f'Population: {population:>30} \n')
            output_file.write(f'Total Confirmed Cases: {confirms:>19} \n')
            output_file.write(f'Total Deaths: {deaths:>28} \n')
            output_file.write(f'Cases per 100,000 people: '
                              f'{cases_per_100k:>18} \n')
            output_file.write(f'Deaths per 100,000 people: '
                              f'{deaths_per_100k:>17} \n')
            output_file.write(f'{paragraph} \n\n')


if __name__ == '__main__':
    main()