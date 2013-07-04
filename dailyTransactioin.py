from stocks.models import Stock, StockTransaction
from django.utils import timezone
import sys,urllib,urllib2
import sys
reload(sys)


stockList = Stock.objects.exclude(status="delist")
print len(stockList)
#encoding=utf-8
for i in range(len(stockList)):
    s= stockList[i]
    print s.code
    url='http://hq.sinajs.cn/list='+s.marketType+s.code
    sData = urllib.urlopen(url).read()
    datas = sData.split(',')
    if len(datas) >=30:
        sname = datas[0]
        sname = sname[sname.index("\"")+1:]
        tranDate=StockHistoryTransaction(code=s.code,name=sname.decode('gbk'),openingPrice=datas[1],closingPrice=datas[3],peakPrice=datas[4],lowestPrice=datas[5],volume=datas[8],transactionAmount=datas[9],transactionDate=datas[30])
        #tranDate.stock=s
        print " opening price-",datas[1]," closingPrice-",datas[3]," peak price-",datas[4]," lowest Price-",datas[5]," volume-",datas[8]," transactionAmount-",datas[9]," transactionDate-",datas[30]
        print tranDate.transactionDate
        tranDate.save();
    else:
        print s.code,"stock is not exist"	
        s.status="delist"
        s.save()
else:
    print 'finished!'


#	url='http://hq.sinajs.cn/list=sh'+s.code
#	s = urllib.urlopen(url).read()
#	datas = s.split(',')
#	print " opening price-",datas[1]," closingPrice-",datas[3]," peak price-",datas[4]," lowest Price-",datas[5]," volume-",datas[8]," transactionAmount-",datas[9]," transactionDate-",datas[30]