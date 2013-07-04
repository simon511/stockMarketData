from stocks.models import Stock, StockHistoryTransaction
from django.utils import timezone
import sys,urllib,urllib2
import os
import codecs
import re
import xml.etree.ElementTree as ET
reload(sys)
#sys.senddefaultencoding("utf-8")
from xml.dom.minidom import parse, parseString

def getHistoryData(stockCode,year,jidu):
    url="http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/"+stockCode+".phtml?year="+str(year)+"\&jidu="+str(jidu)
    print url
    sData = urllib.urlopen(url).read()
    #print sData.find("id=\"FundHoldSharesTable\"")
    if sData.find("id=\"FundHoldSharesTable\"")>0:
        tempStr = sData[sData.index("id=\"FundHoldSharesTable\""):]                       
        #print stock.code+"__"+str(startYear)+"__"+str(startSeason)
        history = tempStr[0:tempStr.find("table")]
        result, number = re.subn("href\=\'(\S+)\'", "", history) 
        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><table "+ result.decode("GBK").encode('utf-8') +"table>"
    else:
        return "";

def paseXMLtoTransactionData(transactionXML):
    root = ET.fromstring(transactionXML)
    transactionList = list()
    for node in root.findall("./tr"):
        element = node.find("./td/div/strong")
        if element is None:
            elementDate = node.find("./td[1]/div/a")
            tranDate =""
            if elementDate is None:
                tranDate = node.find("./td[1]/div").text.strip()
            else:
                tranDate = elementDate.text.strip()
            openPrice = node.find("./td[2]/div").text.strip()
            peakPrice = node.find("./td[3]/div").text.strip()
            closedPrice = node.find("./td[4]/div").text.strip()
            lowestPrice = node.find("./td[5]/div").text.strip()
            volume = node.find("./td[6]/div").text.strip()
            transactionAmount = node.find("./td[7]/div").text.strip()
            tranData=StockHistoryTransaction(openingPrice=openPrice,closingPrice=closedPrice,peakPrice=peakPrice,
                                           lowestPrice=lowestPrice,volume=volume,transactionAmount=transactionAmount,
                                           transactionDate=tranDate )
            transactionList.append(tranData)
        else:
            print element.text
            print "this is header"
    return transactionList

def getStockAllHistoryData(stockCode):
    fileHandle = open("e:/data/"+stockCode+".txt","w+")
    startYear = 2013
    startSeason = 3
    while(startYear>=1991):
        while(startSeason>0):
            print "Season"
            strHistory= getHistoryData(stockCode,startYear,startSeason)
            if len(strHistory)>0:
                l = paseXMLtoTransactionData(strHistory)
                print "count in season",len(l)
                for tData in l:
                    #print tData.transactionDate
                    fileHandle.write(stockCode+", ,"+tData.openingPrice+","+tData.closingPrice+","+tData.peakPrice+
                                     ","+tData.lowestPrice+","+tData.volume+","+tData.transactionAmount+","+
                                     tData.transactionDate+"\n")
            else:
                startYear=1991
                startSeason=0
            startSeason=startSeason-1
            print startSeason
        print "Another "
        startSeason=4
        startYear=startYear-1
    fileHandle.close()
    print "Finalsh :",stockCode
                
            

files=os.listdir(r"e:\data")
shoplist= list()
for file in files:
    shoplist.append(file[0:6])


stockList = Stock.objects.exclude(status="delist")
print len(stockList)
#encoding=utf-8
for i in range(len(stockList)):
    s= stockList[i]
    print s.code
    if s.code in shoplist:
        print s.code
        continue
    #print "getHstockAllHistoryData"
    getStockAllHistoryData(s.code)
else:
    print 'finished!'
    


    



    
                       


