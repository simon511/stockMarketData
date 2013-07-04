from stocks.models import Stock
from django.utils import timezone
import re
import sys
reload(sys)
sys.senddefaultencoding("utf-8")


#encoding=utf-8
''' file format as : aaa(600001) bbb(600003) '''
def getStockCodeFromFile(filePath):
    f = open(filePath)           
    line = f.readline()             
    while line:
        a = re.findall("\S+\(\d{6}\)",line)
        for s in a:
            code = re.search("\(\d{6}\)",s)
            #print code.group(0)
            npos = s.index(code.group(0))
            #print s[0:npos].decode('utf-8')+"-"+s[npos+1:npos+7]
            sname =s[0:npos]
            scode = s[npos+1:npos+7]
            print sname+"_"+scode
            if Stock.objects.filter(code=scode).count()==0 :
                s = Stock(code=scode,name=sname.decode("gbk").encode("utf-8"),listDate=timezone.now(),marketType='sz')
                print sname+"("+scode+")"
                s.save()
        line = f.readline()
    f.close()


getStockCodeFromFile(r"e:/stockcode_sh.txt")
getStockCodeFromFile(r"e:/stockcode_sz.txt")