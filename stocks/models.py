from django.db import models

# Create your models here.
class Stock(models.Model):
    code = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=200)
    companyName = models.CharField(max_length=200,blank=True)
    issueDate = models.DateField('issue date',blank=True)
    listDate = models.DateField('list date',blank=True)
    issuePrice = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    issueAmount =models.BigIntegerField(default=0) 
    marketType = models.CharField(max_length=10)
    status = models.CharField(max_length=20,default='Active')
    type = models.CharField(max_length=20,default='',blank=True)

    def __unicode__(self):
        return self.name+"("+self.code+")"
    def __str__(self):
        return self.__unicode__()	

class StockHistoryTransaction(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    openingPrice = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    closingPrice = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    peakPrice = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    lowestPrice = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    volume = models.BigIntegerField(default=0)
    transactionAmount = models.DecimalField(max_digits=20, decimal_places=2,default=0)	
    transactionDate	= models.DateField('transaction date')