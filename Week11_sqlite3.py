
import sqlite3
import pandas as pd

conn = sqlite3.connect(r'C:\Users\gebruiker\Desktop\data\world.sqlite')

# X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)

# country=input("Baskenti sorgulanacak ülkenin adi: ")
# query = f"SELECT country.Name as CountryName, city.Name as CapitalName  FROM country JOIN city ON country.Capital = city.ID WHERE country.Name = '{country}'"
# df = pd.read_sql_query(query, conn)
# print(df) 


# X şehri hangi ülkede yer almaktadır? (X kullanıcı inputu olacaktır)

# city=input('Ulkesi bulunucak sehir adi:  ')
# query = f"""SELECT city.Name as CityName, country.Name as CountryName 
# FROM city JOIN country ON city.CountryCode = country.Code 
# WHERE city.Name = '{city}'"""
# df = pd.read_sql_query(query, conn)
# conn.close()
# print(df)

# X bölgesinde konuşulan tüm dilleri listeleyin. (X kullanıcı inputu olacaktır)

# region_name= input('Bolge adini giriniz: ')
# query = f"""SELECT DISTINCT countrylanguage.Language as Languages, country.Region
# FROM country
# LEFT JOIN countrylanguage 
# ON country.Code = countrylanguage.CountryCode
# WHERE country.Region = '{region_name}'"""
# df = pd.read_sql_query(query, conn)
# conn.close()
# print(df)

# X dilinin konuşulduğu şehirlerin sayısını bulunuz. (X kullanıcı inputu olacaktır)

# language_name = input('Lutfen bir dil giriniz: ')
# query = f"""
# SELECT COUNT(city.Name) as NumberCity, countrylanguage.Language as LanguageName
# FROM city
# LEFT JOIN countrylanguage 
# ON city.CountryCode = countrylanguage.CountryCode
# WHERE countrylanguage.Language = '{language_name}'
# """
# df = pd.read_sql_query(query, conn)
# conn.close()
# print(df)

# Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın. 
# Eğer bu B dili, A bölgesindeki ülkelerin birinde resmi dil ise, 
# o ülke(ler)in isim(ler)ini listeleyin. 
# Eğer o bölgedeki hiçbir ülkede resmi dil değilse, 
# "B dili A bölgesindeki hiçbir ülkede resmi dil değildir." şeklinde bir çıktı verin. 
# (A ve B kullanıcı inputu olacaktır.)

# region_name= input('Bolge adini giriniz: ')
# language_name = input('Lutfen bir dil giriniz: ')
# query = f"""
# SELECT
# CASE
#     WHEN C.Language = '{language_name}' THEN C.Name
#     ELSE "B dili A bölgesindeki hiçbir ülkede resmi dil değildir."
# END AS sonuc
# FROM (SELECT country.Name, country.Region, countrylanguage.Language
# FROM country
# INNER JOIN countrylanguage
# ON countrylanguage.CountryCode = country.Code
# WHERE countrylanguage.IsOfficial='T' AND country.Region = '{region_name}') AS C
# """
# df = pd.read_sql_query(query, conn)
# conn.close()
# print(df)




# Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz. 
# (Bazı dillerin bir kıtada birden fazla ülkede konuşulduğunu unutmayın ve 
# bunu dikkate alarak bir dili birden fazla kez hesaplamayın.)

# query = f"""
# SELECT country.Continent as ContinentName, 
# COUNT(DISTINCT countrylanguage.Language) as NumberLanguage
# FROM country
# JOIN countrylanguage
# ON country.Code = countrylanguage.CountryCode
# GROUP BY country.Continent
# """
# df = pd.read_sql_query(query, conn)
# conn.close()
# print(df)