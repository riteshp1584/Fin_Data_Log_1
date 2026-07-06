'''

Finance Database Library Studies

https://www.jeroenbouma.com/projects/financedatabase

'''

import financedatabase as fd
from financedatabase import Equities

# db = fd.show_options('equities')

# print(db)

db2 = fd.Equities().select(currency='INR')

print(db2)

db2.to_excel('equities_2.xlsx')

# Works correctly until here
