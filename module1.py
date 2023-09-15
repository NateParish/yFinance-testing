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
            Volume real
            )""")


tickerSymbol = 'AAPL'
dateTime=''
openPrice = 0
highPrice = 0
lowPrice = 0
close = 0
adjClose = 0
volume = 0

df = pd.read_csv(r'Tickers2.csv')
tickerList = df.values.tolist()


#print(tickerList)



#executeLine = "INSERT INTO stockhistory VALUES ('" + tickerSymbol + "', 'test', 75000)"

c.execute("INSERT INTO stockhistory VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)", (tickerSymbol, dateTime, openPrice, highPrice, lowPrice, close, adjClose, volume))

#c.execute("SELECT * FROM stockhistory WHERE Ticker = 'AAPL'")

#print(c.fetchall())

#data = yf.download(tickers='aapl', period='7d', interval='1m')

#df = pd.DataFrame(data)

#data.to_csv('output.csv')
#df.to_csv

#df = pd.read_csv(r'Tickers2.csv')

#tickerList = df.values.tolist()

#print(tickerList)

#print(data)

conn.commit()
conn.close()


