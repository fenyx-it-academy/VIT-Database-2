
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

# 2. X şehri hangi ulkede yer almaktadir? (X kullanıcı inputu olacaktır)

# my_city = input('Enter a city name to find country: ')
# my_cursor.execute(f"""
# SELECT country.Name
# FROM city
# INNER JOIN country
# ON city.CountryCode = country.Code 
# WHERE city.Name = '{my_city}'""")
# my_country_city = my_cursor.fetchall()
# print(my_country_city)

# 3. X bölgesinde konuşulan tüm dilleri listeleyin. (X kullanıcı inputu olacaktır)

# my_region = input('Enter a Region to find languages: ')
# my_cursor.execute(f"""
# SELECT countrylanguage.Language
# FROM country
# INNER JOIN countrylanguage
# ON country.Code = countrylanguage.CountryCode 
# WHERE Region = '{my_region}'
# GROUP BY countrylanguage.Language """)
# languages_of_region = my_cursor.fetchall()
# print(languages_of_region)

#  4. X dilinin konuşulduğu şehirlerin sayısını bulunuz. (X kullanıcı inputu olacaktır)

# my_language = input('Enter a Language to find number of cities: ')
# my_cursor.execute(f"""
# SELECT countrylanguage.Language, count(city.Name)
# FROM country
# JOIN countrylanguage
# ON country.Code = countrylanguage.CountryCode 
# JOIN city
# ON city.CountryCode = country.Code
# WHERE Language = '{my_language}' """)
# number_of_cities = my_cursor.fetchall()
# print(number_of_cities)

# 5.
"""
Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın. Eğer bu B dili, A bölgesindeki ülkelerin birinde resmi dil ise, o ülke(ler)in isim(ler)ini listeleyin. Eğer o bölgedeki hiçbir ülkede resmi dil değilse, "B dili A bölgesindeki hiçbir ülkede resmi dil değildir." şeklinde bir çıktı verin. (A ve B kullanıcı inputu olacaktır.)
"""
# my_region = input('Enter a Region to to examine: ')
# my_language = input('Enter a Language: ')
# my_cursor.execute(f"""
# SELECT country.Name
# FROM country
# JOIN countrylanguage
# ON country.Code = countrylanguage.CountryCode
# WHERE Region = '{my_region}' AND IsOfficial = 'T' AND countrylanguage.Language = '{my_language}' """)
# countries = my_cursor.fetchall()

# if len(countries) > 0:
#     print(countries)
# else:
#     print(f"{my_language}  is not an Official Language in {my_region}.")
    
# 6.

"""
Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz. (Bazı dillerin bir kıtada birden fazla ülkede konuşulduğunu unutmayın ve bunu dikkate alarak bir dili birden fazla kez hesaplamayın.)
"""

my_cursor.execute(f"""
SELECT Continent, count(Language) Number_of_Language
FROM country
JOIN countrylanguage
ON country.Code = countrylanguage.CountryCode
GROUP BY Continent """)
Number_of_Language = my_cursor.fetchall()

for i in Number_of_Language:
    print(f"{i[0]} -> {i[1]} ")


