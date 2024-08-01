mysql -u your_username -p
USE alx_book_store;
SELECT *
FROM customer
WHERE customer_id = 2;
+-------------+------------------+-----------------------+------------------------+
| customer_id | customer_name    | email                 | address                |
+-------------+------------------+-----------------------+------------------------+
|           2 | Blessing Malik   | bmalik@sandtech.com   | 124 Happiness Ave.     |
+-------------+------------------+-----------------------+------------------------+
-- verify_insertion.sql
USE alx_book_store;

SELECT *
FROM customer
WHERE customer_id = 2;
mysql -u your_username -p alx_book_store < verify_insertion.sql

