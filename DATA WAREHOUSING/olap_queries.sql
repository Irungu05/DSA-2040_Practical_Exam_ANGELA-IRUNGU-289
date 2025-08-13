-- Query 1: Total Monthly Sales
SELECT
    td.Year,
    td.Month,
    SUM(sf.TotalSales) AS MonthlySales
FROM
    SalesFact sf
JOIN
    TimeDim td ON sf.InvoiceDate = td.FullDate
GROUP BY
    td.Year,
    td.Month
ORDER BY
    td.Year,
    td.Month;

-- Query 2: Top 10 Customers by Total Spending
SELECT
    cd.CustomerID,
    cd.Country,
    SUM(sf.TotalSales) AS TotalSpending
FROM
    SalesFact sf
JOIN
    CustomerDim cd ON sf.CustomerID = cd.CustomerID
GROUP BY
    cd.CustomerID,
    cd.Country
ORDER BY
    TotalSpending DESC
LIMIT 10;

-- Query 3: Most Popular Products
SELECT
    pd.StockCode,
    pd.Description,
    SUM(sf.Quantity) AS TotalQuantitySold
FROM
    SalesFact sf
JOIN
    ProductDim pd ON sf.StockCode = pd.StockCode
GROUP BY
    pd.StockCode,
    pd.Description
ORDER BY
    TotalQuantitySold DESC
LIMIT 10;