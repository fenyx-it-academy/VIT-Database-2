1 - Siparisleri, siparis veren musterilerin bilgileri ile almak icin bir SQL sorgusu yazin.

     SELECT Orders.OrderID, Customers.*
     FROM Customers
     INNER JOIN Orders
     ON Orders.CustomerID = Customers.CustomerID


2 - Sipariş edilen ürünlerin isimlerini ve ilgili kategorilerini almak icin bir SQL sorgusu yazin.

    SELECT Orders.OrderID, Products.ProductName, Categories.CategoryName
    FROM Products
    INNER JOIN Orders
    ON Orders.ProductID = Products.ProductID
    INNER JOIN Categories
    ON Products.CategoryID = Categories.CategoryID



3 - Müşterilerin müşteri bilgilerini ve varsa sipariş detaylarını almak icin bir SQL sorgusu yazin.

    SELECT Customers.CustomerID, Customers.FirstName, Customers.LastName, Customers.Email, Orders.OrderDate, Orders.OrderID, Orders.ProductID
    FROM Customers
    LEFT JOIN Orders
    ON Customers.CustomerID = Orders.CustomerID



4 - Ürünlerin isimlerini, fiyatlarını ve varsa ilgili kategori adlarını almak icin bir SQL sorgusu yazin.

    SELECT Products.ProductName, Products.Price, Categories.CategoryName
    FROM Products
    LEFT JOIN Categories
    ON Products.CategoryID = Categories.CategoryID



5 - Aynı soyadını paylaşan müşterileri ve bu musterilere ait sipariş detaylarını almak için bir SQL sorgusu yazın.

    SELECT *
    FROM Customers
    INNER JOIN Orders
    ON Customers.CustomerID = Orders.CustomerID
    WHERE Customers.LastName in (SELECT LastName FROM Customers GROUP BY LastName HAVING Count(LastName) > 1)
