import sqlite3

con = sqlite3.connect('../database')

print("Enter ID: ")
r = input()

print("Enter Email: ")
nm = input()

print("Enter UserName: ")
un = input()

print("Enter Password: ")
ph = input()

print("Enter Date Joined: ")
dj = input()

print("Enter Cart Items: ")
ci = input()

print("Enter Orders: ")
od = input()

query = """insert into customer(id, email, username, password_hash, date_joined, cart_items, orders) VALUES (?, ?, ?, ?, ?, ?, ?)"""

con.execute(query, (r, nm, un, ph, dj, ci, od))
con.commit()
con.close()
print("Data Saved.... ")
