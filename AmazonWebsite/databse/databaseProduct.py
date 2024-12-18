import sqlite3

con = sqlite3.connect('../database')

print("Enter ID: ")
a = input()

print("Enter Product Name: ")
b = input()

print("Enter Current Price: ")
c = input()

print("Enter Previous Price: ")
d = input()

print("Enter In Stock: ")
e = input()

print("Enter Product Picture: ")
f = input()

print("Enter Flash Sale: ")
g = input()

print("Enter Date Added: ")
h = input()

query = """insert into product(id, product_name, current_price, previous_price, in_stock, product_picture, flash_sale, date_added) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

con.execute(query, (a, b, c, d, e, f, g, h))
con.commit()
con.close()
print("Data Saved.... ")