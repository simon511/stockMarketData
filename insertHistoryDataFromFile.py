from stocks.models import Stock, StockHistoryTransaction
from django.utils import timezone
import sys,urllib,urllib2 


files =os.listdir(r"e:\data")
for file in files:
    s = Stock.objects.get(code=file[0:6])
    fileHandle=open(r"e:\data\\"+s.code+".txt")
    print s.code
    while 1:
        line = fileHandle.readline()
        if not line:
            break
        sData = line.split(",")
        if sData[8].find("2004-") ==0 :
            print s.code," finished "
            break
        tranData=StockHistoryTransaction(code=s.code,name=s.name)
        if StockHistoryTransaction.objects.filter(code=s.code,transactionDate=sData[8]).count()==0 :
            tranData.openingPrice=sData[2]
            tranData.closingPrice=sData[3]
            tranData.peakPrice=sData[4]
            tranData.lowestPrice=sData[5]
            tranData.volume=sData[6]
            tranData.transactionAmount=sData[7]
            tranData.transactionDate=sData[8]
            tranData.save()
        else:
            print "already exists",s.code,sData[8]
            
print "finished"



