import urllib.request
import re
from yahoo_finance import Share
data=[]
x=0

file = open("symbol1.txt")
line = file.read()
words = line.split()
print(words)
print(len(words))
for i in words:
    print("    ")
    symbol=words[x]
    yahoo = Share(symbol)
    print("price of "+symbol+":")
    #print (yahoo.get_open())
    print (yahoo.get_price())
    print("trade_datetime"+symbol+":")
    print (yahoo.get_trade_datetime())
    x=x+1





