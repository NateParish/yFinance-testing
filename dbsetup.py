import sqlite3


def CreateDatabase():

    conn = sqlite3.connect('stockdata.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE stockhistory(
                EntryID text,
                Ticker text,
                Datetime text,
                Open real,
                High real,
                Low real,
                Close real,
                AdjClose real,
                Volume real,
                DateEntered text
                )""")


    
    conn.commit()
    conn.close()