import sqlite3

con = sqlite3.connect('../database')

print("Enter ID: ")
i = input()

print("Enter Quantity: ")
q = input()

print("Enter Price: ")
w = input()

print("Enter Status: ")
z = input()

print("Enter PayMent ID: ")
m = input()

print("Enter Customer Link: ")
c = input()

print("Enter Product Link: ")
y = input()

query = """insert into "Order"(id, quantity, price, status, payment_id, customer_link, product_link) VALUES (?, ?, ?, ?, ?, ?, ?)"""

con.execute(query, (i, q, w, z, m, c, y))
con.commit()
con.close()
print("Data Saved.... ")