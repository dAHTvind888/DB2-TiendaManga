CREATE DATABASE Manga_Store_BD2;

USE Manga_Store_BD2;

CREATE TABLE MANGA (
    Id_Manga INT IDENTITY(1,1) PRIMARY KEY,
    Manga_name VARCHAR(255),
    Author_name VARCHAR(255),
    Genre VARCHAR(255),
    Publish_date DATE,
    Modified_date DATE,
	Estado INT
);

CREATE TABLE VOLUME (
    Id_Volume INT IDENTITY(1,1) PRIMARY KEY,
    Volume_nro INT,
    Release_date DATE,
    Price INT,
    Stock INT,
    Id_Manga INT,
    Modified_date DATE,
	Estado INT,
    CONSTRAINT FK_Volume_Manga FOREIGN KEY (Id_Manga) REFERENCES MANGA(Id_Manga)
);

CREATE TABLE CUSTOMER (
    Id_Customer INT IDENTITY(1,1) PRIMARY KEY,
    Customer_name VARCHAR(255),
    Customer_first_surname VARCHAR(255),
    Customer_second_surname VARCHAR(255),
    NIT INT,
    Email VARCHAR(255),
    Customer_Birthday DATE,
    Modified_date DATE
);

CREATE TABLE EMPLOYEE (
    Id_Employee INT IDENTITY(1,1) PRIMARY KEY,
    Employee_name VARCHAR(255),
    Employee_first_surname VARCHAR(255),
    Employee_second_surname VARCHAR(255),
    Wage INT,
    Hired_date DATE,
    Email VARCHAR(255),
    Phone_number INT,
    Modified_date DATE,
	Estado INT
);

CREATE TABLE SALES_DETAILS (
    Id_Sales INT IDENTITY(1,1) PRIMARY KEY,
    Id_Customer INT,
    Id_Employee INT,
    Sales_date DATE,
    Total_price INT,
    Modified_date DATE,
    CONSTRAINT FK_SalesDetails_Customer FOREIGN KEY (Id_Customer) REFERENCES CUSTOMER(Id_Customer),
    CONSTRAINT FK_SalesDetails_Employee FOREIGN KEY (Id_Employee) REFERENCES EMPLOYEE(Id_Employee)
);

CREATE TABLE SALES (
    Id_Sales INT,
    Id_Volume INT,
    Quantity INT,
    Modified_date DATE,
    PRIMARY KEY (Id_Sales, Id_Volume),
    CONSTRAINT FK_Sales_Volume FOREIGN KEY (Id_Volume) REFERENCES VOLUME(Id_Volume),
    CONSTRAINT FK_Sales_SalesDetails FOREIGN KEY (Id_Sales) REFERENCES SALES_DETAILS(Id_Sales)
);