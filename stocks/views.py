from django.http import HttpResponse
from django.template import RequestContext, loader
from stocks.models import Stock, StockHistoryTransaction

def index(request):
    latest_stock_list = Stock.objects.order_by('code')[:25]
    template = loader.get_template('stocks/index.html')
    context = RequestContext(request, {
        'latest_stock_list': latest_stock_list,
    })
    return HttpResponse(template.render(context))