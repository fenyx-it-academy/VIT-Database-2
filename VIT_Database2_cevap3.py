import sqlite3
import pandas as pd

# db ye baglanma
conn = sqlite3.connect("C:/Users/test/Documents/ARBEID/SQL/world.sqlite")


# # 1- X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)
# country = input("Hangi ulkenin baskentini bilmek istersiniz?\n")
# query = f"SELECT city.Name from city JOIN country on city.ID=country.Capital where country.Name = '{country}'"
# data = pd.read_sql(query, conn)
# print(f"Girdiginiz ulke:{country}, Baskenti:{data}")


# # 2- X şehri hangi ulkede yer almaktadir? (X kullanıcı inputu olacaktır)
# city = input("Hangi sehir hangi ulkede bilmek icin sehir adini girin:\n")
# query = f"SELECT country.Name FROM city JOIN country on city.CountryCode=country.Code where city.Name = '{city}'"
# data = pd.read_sql(query, conn)
# print(f"Girdiginiz sehir:{city}, bulundugu ulke:{data}")


# # 3- X bölgesinde konuşulan tüm dilleri listeleyin. (X kullanıcı inputu olacaktır)
# region1 = input("Bolgede konusulan dilleri ogrenmek icin bolgeyi girin:\n")
# query = f"""SELECT country.Region, country.Name, countrylanguage.Language
# FROM country
# JOIN countrylanguage on country.Code = countrylanguage.CountryCode
# WHERE country.Region = '{region1}'"""
# data = pd.read_sql(query, conn)
# print(data)


# # 4- X dilinin konuşulduğu şehirlerin sayısını bulunuz. (X kullanıcı inputu olacaktır)
# language = input("Hangi dilin kac tane sehirde konusuldugunu ogrenmek istersiniz?:\n")
# query = f"""SELECT countrylanguage.Language, country.Name as Country_Name, city.Name as City_Name
# FROM countrylanguage
# JOIN country on country.Code = countrylanguage.CountryCode
# JOIN city on country.Code = city.CountryCode
# WHERE countrylanguage.Language = '{language}'"""
# data = pd.read_sql(query, conn)
# print(data)


# 5- Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın.
# Eğer bu B dili, A bölgesindeki ülkelerin birinde resmi dil ise, o ülke(ler)in isim(ler)ini listeleyin.
# Eğer o bölgedeki hiçbir ülkede resmi dil değilse, "B dili A bölgesindeki hiçbir ülkede resmi dil değildir."
# şeklinde bir çıktı verin. (A ve B kullanıcı inputu olacaktır.)


# 6- Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz.
# (Bazı dillerin bir kıtada birden fazla ülkede konuşulduğunu unutmayın ve
# bunu dikkate alarak bir dili birden fazla kez hesaplamayın.)


conn.close()  # Kapatma komutu
