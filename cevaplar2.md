1 - "city" ve "country" tablolarını düşünün. Nüfusu 1 milyondan fazla olan her şehrin adını, ilgili ülke adını ve nüfusunu almak için bir SQL sorgusu yazın.

SELECT city.Name as 'City', country.Name as 'Country', city.Population 
FROM city
INNER JOIN country
ON city.CountryCode = country.Code
WHERE city.Population > 1000000



2 - "city," "country" ve "countrylanguage" tablolarını kullanarak her ülkenin toplam nüfusunu ve resmi dil olarak İngilizce konuşan nüfusun yüzdesini almak için bir SQL sorgusu yazın. Sonuçları nüfusa göre azalan şekilde sıralayın.


SELECT country.name, country.Population, countrylanguage.Percentage as 'English speaking percentage'
FROM country
INNER JOIN countrylanguage
ON country.Code = countrylanguage.CountryCode
WHERE countrylanguage.Language = 'English' AND countrylanguage.IsOfficial = 'T' 
ORDER BY Population DESC


3 - "city" ve "country" tablolarını düşünün. Her şehrin adını, ilgili ülke adını, kıtasını ve yönetim şeklini almak için bir SQL sorgusu yazın. Yalnızca "Anayasal Monarşi" (Constitutional Monarchy) yönetim şekline sahip olan şehirleri dahil edin.


SELECT city.Name as 'City', country.Name as 'Country', country.Continent ,country.GovernmentForm
FROM city
INNER JOIN country
ON city.CountryCode = country.Code
WHERE country.GovernmentForm = 'Constitutional Monarchy'



4 - "city," "country" ve "countrylanguage" tablolarını kullanarak her şehrin adını, ilgili ülke adını ve resmi dil dışında konuşan nüfusun yüzdesini almak için bir SQL sorgusu yazın. Yalnızca yüzdesi %10'dan büyük olan şehirleri dahil edin.


SELECT country.Code, city.Name as 'City', country.Name as 'Country', countrylanguage.Percentage
FROM city
INNER JOIN country
ON city.CountryCode = country.Code
INNER JOIN countrylanguage
ON country.Code = countrylanguage.CountryCode
WHERE countrylanguage.IsOfficial = 'F' AND countrylanguage.Percentage > 10




5 - "city" ve "country" tablolarını düşünün. Her şehrin adını, ilgili ülke adını, bölgesini ve devlet başkanını almak için bir SQL sorgusu yazın. Yalnızca nüfusu 100 milyondan fazla olan bölgelerde bulunan şehirleri dahil edin.


SELECT city.Name as 'City', country.Name as 'Country', country.Region , country.HeadOfState
FROM city
INNER JOIN country
ON city.CountryCode = country.Code
WHERE country.Region in (SELECT region FROM country GROUP BY Region HAVING SUM(Population) > 100000000)