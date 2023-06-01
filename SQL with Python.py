import sqlite3 as sql
conn = sql.connect('world.sqlite')

c = conn.cursor()
# c.execute('SELECT country.Name FROM country')
# tum_liste = c.fetchall()
# print(tum_liste)
# for country in tum_liste:
#     print(country)

# x= input("Ulke Adi:")
conn = sql.connect('world.sqlite')
c = conn.cursor()
# c.execute("""
#     SELECT city.Name as CityName, country.Name as CountryName
#     FROM city
#     LEFT JOIN country on city.ID = country.Capital
#     WHERE country.Name IS NOT NULL
#     """)
# liste = c.fetchall()
# for capital in liste:
#     if x == capital[1]:
#         print(capital)
#####################################################################
# y = input("City Name:")
# c.execute("""
# SELECT city.Name as CityName, country.Name as CountryName
# FROM city
# LEFT JOIN country on city.CountryCode= country.Code

# """)
# newlist = c.fetchall()
# for city in newlist:
#     if y == city[0]:
#         print(city)

#####################################################################
# z = input("Country Name:")
# c.execute("""
# SELECT countrylanguage.Language, country.Name as CountryName
# FROM countrylanguage
# LEFT JOIN country on countrylanguage.CountryCode = country.Code

# """)
# languageList = c.fetchall()
# for language in languageList:
#     if z == language[1]:
#         print(language)
#######################################################################
# dil = input("Language:")
# bolge = input("Region Name:")
# c.execute("""
# SELECT country.Name, country.Region, countrylanguage.Language, countrylanguage.IsOfficial
# FROM country
# LEFT JOIN countrylanguage on country.Code = countrylanguage.CountryCode
# """)
# region = c.fetchall()
# for i in region:
#     if bolge == i[1]:
#         if dil == i[2]:
#             if i[3] == "T":
#                 print(i[0])
#             elif i[3] == "F":
#                 pass
#             else:
#                 print(f"{dil} dili {bolge} bölgesindeki hiçbir ülkede resmi dil değildir.")
#         else:
#             pass
#     else:
#         pass
########################################################################################

# c.execute("""
# SELECT country.Continent ,  count(DISTINCT countrylanguage.Language) as TotalLanguage
# FROM country
# LEFT JOIN countrylanguage on country.Code = countrylanguage.CountryCode
# GROUP By country.Continent
# """)
# Continent = c.fetchall()
# for l in Continent:
#     print(l)
