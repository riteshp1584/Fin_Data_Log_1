'''

Finance Database Library Studies

https://www.jeroenbouma.com/projects/financedatabase

'''

import financedatabase as fd

funds_db = fd.Funds()

f1 = funds_db.show_options()

# print(f1)


f2 = funds_db.select(currency='GBP', category_group='Fixed Income')

print(f2)

'''
print(f2['market'])

f2['market'].to_excel('ctest_4.xlsx')

# Works correctly until here

'''
