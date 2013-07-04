from stocks.models import Stock, StockHistoryTransaction
from django.utils import timezone
import sys,urllib,urllib2
import sys


files =os.listdir(r"e:\data2")
for file in files:
    s = Stock.objects.filter(code=file[0:6])
    tranData=StockHistoryTransaction(code=s.code,name=s.name)
    fileHandle=open(r"e:\data2\\"+s.code+".txt")
    while 1:
        line = fileHandle.readline
        if not line:
            break
        sData = line.split(",")
        print sData

'''
       if StockHistoryTransaction.objects.filter(code=s.code,transactionDate=sData[8]).count()==0:
            
            tranData.openingPrice=sData[2]
            tranData.closingPrice=sData[3]
            tranData.peakPrice=sData[4]
            tranData.lowestPrice=sData[5]
            tranData.volume=sData[6]
            tranData.transactionAmount=sData[7]
            tranData.transactionDate=sData[8]
            tranData.save()
        else:
            print "already exists"

'''


