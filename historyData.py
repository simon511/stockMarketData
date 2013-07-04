from stocks.models import Stock, StockHistoryTransaction
from django.utils import timezone
import sys,urllib,urllib2
import sys
reload(sys)
sys.senddefaultencoding("utf-8")
url='http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/600200.phtml?year=2013&jidu=1'
sData = urllib.urlopen(url).read()
print sData