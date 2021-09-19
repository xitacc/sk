import pathlib
from sqlite3 import *
import sys
from os import *

sqli3_path = pathlib.Path("C:\\Users\\cxd\\Desktop\\SSD Backup\\MCWebsite\\MCWebsiteP\\db.sqlite3")
print(sqli3_path.absolute())
con_ = connect(sqli3_path)
cur_ = con_.cursor()
table_book = "MCWebsiteA_book"

cur_.execute("select * from " + table_book )

print([book for book in cur_.fetchall()])
cur_.execute("PRAGMA table_info("+table_book+")") # Achtung zur Abfrage .fetchall()
res_list = cur_.fetchall()

print(res_list)
print(f"{res_list}")
# res = [info for info in res_book_info]
# print(res)
# print(res_book_info.fetchall())

# table_site = "MCWebsiteA_site"
# res_site = cur_.execute("select * from " + table_site + " where book_id=? ", (1,))
# for row in res_site:
#
#     print(row)
