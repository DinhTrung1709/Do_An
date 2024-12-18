import sqlite3

con = sqlite3.connect('../database')

print("Enter ID: ")
i = input()

print("Enter Quantity: ")
q = input()

print("Enter Customer Link: ")
c = input()

print("Enter Product Link: ")
p = input()

query = """insert into cart(id, quantity, customer_link, product_link) VALUES (?, ?, ?, ?)"""

con.execute(query, (i, q, c, p))
con.commit()
con.close()
print("Data Saved.... ")