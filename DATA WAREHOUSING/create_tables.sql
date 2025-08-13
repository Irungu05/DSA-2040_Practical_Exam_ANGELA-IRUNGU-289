-- Create Time Dimension Table
CREATE TABLE TimeDim (
    TimeID INTEGER PRIMARY KEY,
    Date DATE,
    Day INTEGER,
    Month INTEGER,
    Quarter INTEGER,
    Year INTEGER
);

-- Create Customer Dimension Table
CREATE TABLE CustomerDim (
    CustomerID TEXT PRIMARY KEY,
    CustomerName TEXT,
    CustomerCountry TEXT
);

-- Create Product Dimension Table
CREATE TABLE ProductDim (
    ProductID TEXT PRIMARY KEY,
    ProductName TEXT,
    ProductCategory TEXT
);

-- Create Sales Fact Table
CREATE TABLE SalesFact (
    InvoiceNo TEXT,
    CustomerID TEXT,
    ProductID TEXT,
    TimeID INTEGER,
    Quantity INTEGER,
    UnitPrice REAL,
    TotalSales REAL,
    FOREIGN KEY (CustomerID) REFERENCES CustomerDim(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES ProductDim(ProductID),
    FOREIGN KEY (TimeID) REFERENCES TimeDim(TimeID)
);