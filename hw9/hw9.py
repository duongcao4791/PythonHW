import urllib.request
import urllib.parse
import bs4
import re
import pandas as pd


def process_num(num):
    return int(re.sub(r'[^\w\s.]', '', num))


def process_str(str):
    return re.sub(r'(\[\w])|(\[]?\w.])', '', str)


def visit_url(url):
    """
    Open the given url and return its visible content and the referenced links
    :param url:(string) - the address of the web page to be read
    :return: (tuple) (text, links)
        text: a string containing the visible content of the corresponding web page.
        absolute_links: a set of strings containing the referenced absolute links.
        None if there is an error opening the url.
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
    URL = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
    soup = visit_url(URL)
    tables = soup.find_all('table')
    # Create array to hold the data we extract
    countries = []
    populations = []

    for table in tables:
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')

            if len(cells) > 1:
                country = cells[1]
                countries.append(process_str(country.text.strip()))

                population = cells[2]
                populations.append(process_num(population.text.strip()))

    df1 = pd.DataFrame(populations, index=countries, columns=['Population'])
    match = df1[df1.index.str.contains(search, case=False)]
    return match


def get_case(search):
    URL = 'https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic_by_country_and_territory'
    soup = visit_url(URL)
    tables = soup.find_all('table', {'id': "thetable"})

    # Create array to hold the data we extract
    countries = []
    confirms = []
    deaths = []

    for table in tables:
        rows = table.find_all('tr')

        for row in rows:
            names = row.find_all('th')
            cells = row.find_all('td')

            if len(names) == 2:  # skip 2 first rows
                country = names[1]
                countries.append(process_str(country.text.strip()))

            if len(cells) > 1:
                confirm = cells[0]
                confirms.append(process_num(confirm.text.strip()))

                death = cells[1]
                deaths.append(process_num(death.text.strip()))

    df2 = pd.DataFrame({'Total Confirm Case': confirms,
                        'Total Deaths': deaths}, index=countries)
    match = df2[df2.index.str.contains(search, case=False)]
    return match


def cases_per_pop(cases, pop):
    return 100000 * cases / pop


def deaths_per_pop(deaths, pop):
    return 100000 * deaths / pop


def main():
    search_term = input('Please enter a search term: ')
    pop = get_population(search_term)
    cases = get_case(search_term)

    # write output
    with open(f'{search_term}summary.txt', 'w', encoding='utf-8') as output_file:
        for i in range(len(pop)):
            country = pop.index[i]
            population = pop["Population"][i]
            confirms = cases['Total Confirm Case'][i]
            deaths = cases['Total Deaths'][i]

            output_file.write(f'Country: {country} \n')
            output_file.write(f'Population: {population:,d} \n')
            output_file.write(f'Total Confirmed Cases: {confirms:,d} \n')
            output_file.write(f'Total Deaths: {deaths:,d} \n')
            output_file.write(f'Cases per 100,000 people: {cases_per_pop(confirms, population):,.1f} \n')
            output_file.write(f'Deaths per 100,000 people: {deaths_per_pop(deaths, population):,.1f} \n\n')


if __name__ == '__main__':
    main()
