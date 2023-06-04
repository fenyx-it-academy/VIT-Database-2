import sqlite3
import pandas as pd

# db ye baglanma
conn = sqlite3.connect("C:\\Users\\cfrdm\\Desktop\\ViT\\SQL\\week11\\world.sqlite")

# sorguları calıstırmak için config islemleri
c = conn.cursor()

# 1-) X ülkesinin başkenti neresidir? (X kullanıcı inputu olacaktır)

capital = input("Başkentini öğrenmek istediğiniz ülkeyi yazınız :")

df = pd.read_sql(f"""

SELECT city.Name
FROM country
INNER JOIN city
ON country.Capital = city.ID
WHERE country.Name = '{capital}'

""",conn)

print(df)

# 2-) X şehri hangi ulkede yer almaktadir? (X kullanıcı inputu olacaktır)

city = input("Ülkesini öğrenmek istediğin şehiri giriniz : ")

df = pd.read_sql(f"""
SELECT country.Name
FROM country
INNER JOIN city
ON country.Code = city.CountryCode
WHERE city.Name = '{city}'
""",conn)
print(df)

# 3-) X bölgesinde konuşulan tüm dilleri listeleyin. (X kullanıcı inputu olacaktır)

df = pd.read_sql(f"""
SELECT region
FROM country
Group BY region

""",conn)

print(df)

region = input("Kullanılan dilleri öğrenmek için bir bölge ismi giriniz  :")
df = pd.read_sql(f"""
SELECT countrylanguage.Language
FROM country
INNER JOIN countrylanguage
ON country.Code = countrylanguage.CountryCode
WHERE country.Region = '{region}'
""",conn)

print(df)

# 4-) X dilinin konuşulduğu şehirlerin sayısını bulunuz. (X kullanıcı inputu olacaktır)

language = input("Dil :")

df = pd.read_sql(f"""
SELECT city.Name
FROM country
INNER JOIN countrylanguage
ON country.Code = countrylanguage.CountryCode
INNER JOIN city
ON countrylanguage.CountryCode = city.CountryCode
WHERE countrylanguage.Language = '{language}'
""",conn)

print(df)

# 5-) Kullanıcıdan bir A bölgesi(region) ve bir B dili(language) alın. Eğer bu B dili, A bölgesindeki ülkelerin birinde resmi dil ise, o ülke(ler)in isim(ler)ini listeleyin. 
# Eğer o bölgedeki hiçbir ülkede resmi dil değilse, "B dili A bölgesindeki hiçbir ülkede resmi dil değildir." şeklinde bir çıktı verin. (A ve B kullanıcı inputu olacaktır.)

region = input("Bölge ismi giriniz :")

language = input("Dil giriniz :")

df = pd.read_sql(f"""
SELECT country.name
FROM country
INNER JOIN countrylanguage
ON country.Code =  countrylanguage.CountryCode
WHERE country.Region = '{region}' AND countrylanguage.Language = '{language}' AND countrylanguage.IsOfficial = 'T'
""",conn)

print(df)

if df.empty == True:
    print("B dili A bölgesindeki hiçbir ülkede resmi dil değildir.")

# 6-) Tüm kıtaları, o kıtalarda konuşulan dillerin sayısı ile birlikte bulunuz. 
# (Bazı dillerin bir kıtada birden fazla ülkede konuşulduğunu unutmayın ve bunu dikkate alarak bir dili birden fazla kez hesaplamayın.)


df = pd.read_sql("""
SELECT country.Continent, count(DISTINCT(countrylanguage.Language))
FROM country
INNER JOIN countrylanguage
ON country.Code =  countrylanguage.CountryCode
GROUP BY country.Continent
""",conn)

print(df)



