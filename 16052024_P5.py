'''

Finance Database Library Studies

https://www.jeroenbouma.com/projects/financedatabase

'''

import financedatabase as fd

curr = fd.Currencies()

c1 = curr.show_options()

# print(c1)

c2 = curr.select(base_currency='USD',quote_currency='SGD')

print(c2)

# c2.to_excel('c_test6.xlsx')

# Works correctly until here
