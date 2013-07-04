import xml.etree.ElementTree as ET
import sys,urllib,urllib2
import os
from xml.dom.minidom import parse, parseString

def getCompanyData(marketType,stockCode):
    url="http://f10.eastmoney.com/f10_v2/CompanySurvey.aspx?code="+marketType+stockCode
    print url
    sData = urllib.urlopen(url).read()
    #print sData.find("id=\"FundHoldSharesTable\"")
    if sData.rfind("<div class=\"content\">")>0:
        tempStr = sData[sData.rindex("<div class=\"content\">"):]                       
        #print stock.code+"__"+str(startYear)+"__"+str(startSeason)
        if tempStr.find("<table>")>0 :
            history = tempStr[0:tempStr.find("</table>")]
            #print tempStr
            return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"+ history +"</table></div>"
        else:
            return ""
    else:
        return "";


companyInfo=getCompanyData("sz","150011")
if len(companyInfo) >0:
    root =ET.fromstring(companyInfo)
    listDate=root.find("table/tr[1]/td[2]").text.strip()
    issueDate=root.find("table/tr[2]/td[2]").text.strip()
    issueAmount=root.find("table/tr[4]/td[1]").text.strip()
    issuePrice=root.find("table/tr[4]/td[2]").text.strip()
    issueAmount = issueAmount.encode("utf-8").replace("亿".decode("gbk").encode("utf-8"),"00000000")
    issueAmount = issueAmount.replace("万".decode("gbk").encode("utf-8"),"0000")
    print issueAmount.encode("utf-8")
    print "亿".decode("gbk").encode("utf-8")
    print issueAmount.encode("utf-8").replace("亿".decode("gbk").encode("utf-8"),"0000")
    print issuePrice
