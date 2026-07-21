'''

Finance Database Library Studies

https://www.jeroenbouma.com/projects/financedatabase

'''

import financedatabase as fd

equities = fd.Equities()

eq_db1 = equities.show_options(country='India')

print(eq_db1)

# Use help(fd.Equities()) to get more info about all Methods and Arguments

# Works correctly until here

