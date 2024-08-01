sql = "INSERT INTO customer table ( customer_id, customer_name, email, adress) VALUES (%s, %s)"
val = (1, 'cole Baidoo, 'cbaidoo@sandteech.com', '123 Happiness Ave.')
mycursor.execute(sql, val)
