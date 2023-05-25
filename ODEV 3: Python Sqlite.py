import sqlite3
import pandas as pd

# Veritabanına bağlanma
conn = sqlite3.connect('world.sqlite')

#1- X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)

# ulke=input('bir ülke ismi giriniz:  ')
# query = f"SELECT country.Name, city.Name  FROM country JOIN city ON country.Capital = city.ID WHERE country.Name = '{ulke}'"
# df = pd.read_sql_query(query, conn)
# print(df) 

-------------------

#2- X şehri hangi ülkede yer almaktadır? (X kullanıcı inputu olacaktır)
-----------
# sehir=input('Sehir İsmi Giriniz:  ')
# query = f"SELECT city.Name, country.Name  FROM city JOIN country ON city.CountryCode = country.Code WHERE city.Name = '{sehir}'"
# df = pd.read_sql_query(query, conn)
# conn.close()
# print(df)

-----------------------------

#3- X bölgesinde konuşulan tüm dilleri listeleyin. (X kullanıcı inputu olacaktır)

# bolge=input('Bolge İsmi Giriniz:  ')
# query = f"SELECT countrylanguage.Language FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Region = '{bolge}'"
# df = pd.read_sql_query(query, conn)
# print(df) 

-------------------------------------

# 4- X dilinin konuşulduğu şehirlerin sayısını bulunuz. (X kullanıcı inputu olacaktır)
# sehir_dil=input('Konusulan dil giriniz:  ')
# query = f"SELECT COUNT(*) as NumberOfCities FROM city JOIN countrylanguage ON city.CountryCode = countrylanguage.CountryCode WHERE countrylanguage.Language = '{sehir_dil}'"
# df = pd.read_sql_query(query, conn)
# print(df) 

------------------------------------------------------

# 5-Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın.
# Eğer bu B dili, A bölgesindeki ülkelerin birinde resmi dil ise, o ülke(ler)in isim(ler)ini listeleyin.
# Eğer o bölgedeki hiçbir ülkede resmi dil değilse, "B dili A bölgesindeki hiçbir ülkede resmi dil değildir." şeklinde bir çıktı verin. (A ve B kullanıcı inputu olacaktır.)

# bolge=input('Lütfen bölge ismi giriniz:   ')
# dil=input('Lütfen dil giriniz:   ')
# query = f"SELECT country.Name FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Region = '{bolge}' AND countrylanguage.Language = '{dil}' AND countrylanguage.IsOfficial = 'T'"
# df = pd.read_sql_query(query, conn)
# if df.empty:
#     print(f"{dil} dili {bolge} bölgesindeki hiçbir ülkede resmi dil değildir.")
# else:
#     print(df)

-----------------------------------

# 6-Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz.
#query = "SELECT country.Continent as Kıtalar, COUNT(DISTINCT countrylanguage.Language) as KonuşulanDilSayısı FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode GROUP BY country.Continent"
#df = pd.read_sql_query(query, conn)
#print(df) 
