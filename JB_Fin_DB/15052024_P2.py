'''

Finance Database Library Studies

https://www.jeroenbouma.com/projects/financedatabase

'''

import financedatabase as fd

equities = fd.Equities()

india_companies = equities.select(country='India', sector='Energy')

# print(india_companies.columns)

# print(india_companies)

output = fd.show_options("equities")

print(output)   # To get parameter lists such as country lists etc.

# List of currencies

currency_list = output["currency"]

for currency in currency_list:
    print(currency)

# List of countries

country_list = output['country']

for x in country_list:
    print(x)

# List of sectors

sector_list = output['sector']

for x in sector_list:
    print(x)
