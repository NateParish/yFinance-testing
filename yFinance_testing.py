import yfinance as yf
import sqlite3
import pandas as pd
import datetime
import dbsetup

setupDatabase = True


conn = sqlite3.connect('stockdata.db')
c = conn.cursor()

if setupDatabase == True:
    dbsetup.CreateDatabase()


tickerList = pd.read_csv('Tickers2.csv')

for i in range(len(tickerList)):
    print(tickerList.loc[i,'TICKER SYMBOL'])

    ticker = tickerList.loc[i,'TICKER SYMBOL']
    dateTimeOrig = ''
    dateTime = ''
    openPrice = 0
    highPrice = 0
    lowPrice = 0
    close = 0
    adjClose = 0
    volumeSecondTry = 0
    volume = 0
    dateEntered = datetime.datetime.now().strftime("%B %d, %Y %I:%M%p")


    #df = pd.read_csv(r'output.csv')
    df = yf.download(tickers='tsla', period='7d', interval='1m')

    CSVpath = 'CSVFiles/' + ticker + '.csv'

    df.to_csv(CSVpath)

    df = pd.read_csv(CSVpath)

    for i in range(len(df)):

        ticker = ticker
        dateTimeOrig = df.loc[i, 'Datetime']
        entryid = ticker + dateTimeOrig
        dateTime = dateTimeOrig[:19]
        openPrice = df.loc[i, 'Open']
        highPrice = df.loc[i, 'High']
        lowPrice = df.loc[i, 'Low']
        close = df.loc[i, 'Close']
        adjClose = df.loc[i, 'Adj Close']
        volume = df.loc[i, 'Volume']
        dateEntered = datetime.datetime.now().strftime("%B %d, %Y %I:%M%S%p")

        c.execute("INSERT INTO stockhistory VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (entryid, ticker, dateTime, openPrice, highPrice, lowPrice, close, adjClose, float(volume), dateEntered))
        #print(volume)

        #print(entryid)
    conn.commit()

c.execute("SELECT * FROM stockhistory WHERE Ticker = 'AMZN'")
df2 = c.fetchall()

print(df2)


conn.commit()
conn.close()