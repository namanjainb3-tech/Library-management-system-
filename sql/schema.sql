CREATE DATABASE IF NOT EXISTS Library_Management_System;

USE Library_Management_System;

CREATE TABLE customer_details(
    C_id INT,
    C_Name VARCHAR(15),
    Ph_no VARCHAR(10),
    Book_issued INT,
    Issue_date VARCHAR(12),
    Return_Date VARCHAR(12),
    Member CHAR(1),
    Membership INT
);

CREATE TABLE book_details(
    b_id INT,
    b_name VARCHAR(25),
    publication VARCHAR(50),
    author VARCHAR(15),
    status VARCHAR(20),
    reviews DECIMAL(5,3)
);
