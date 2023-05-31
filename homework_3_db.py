import sqlite3 as sql

my_db = sql.connect('world.sqlite')
my_cursor = my_db.cursor()

#  1. X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)

# my_country = input('Enter a country name to find capital city: ')
# my_cursor.execute(f"""
# SELECT city.Name
# FROM city
# INNER JOIN country
# ON city.ID = country.Capital 
# WHERE country.Name = '{my_country}'""")
# capital_city = my_cursor.fetchall()
# print(capital_city)


