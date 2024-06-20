from django.db import models

# Create your models here.

class Paymentdetail(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    order_no = models.IntegerField()
    total_cost = models.FloatField(default=0.0)
    payment_status = models.CharField(max_length=50, default='paid')
    useremail = models.CharField(max_length=50, default=None)
