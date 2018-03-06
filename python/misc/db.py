# simple db code to get started with sqlite3
# Uses code from the official docs: 
# https://docs.python.org/2/library/sqlite3.html

import sqlite3
import random

conn = sqlite3.connect('example.db')
c = conn.cursor()

class SqlTable:
    tid = 0
    name = 'uninitialised'
    fields = []

    def __init__(self, name, fields):
        self.tid = random.randint(1,100)
        self.name = name
        self.fields = fields

    def __repr__(self):
        return 'SqlTable(name = %r, fields = %r)' % (self.name, self.fields)

def createBlank():
    c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')

def addExampleData():
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
    conn.commit()

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

stocksTable = SqlTable(name = 'Stocks', fields = ['date text', 'trans text', 'symbol text', 'qty real', 'price real'])
print(stocksTable)

conn.close()
