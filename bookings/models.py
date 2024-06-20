from django.db import models
from datetime import date

# Create your models here.
class Bookinghotel(models.Model):

    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    contact_no = models.CharField(max_length=13)
    no_people = models.IntegerField()
    no_rooms = models.IntegerField(default=0)
    start = models.DateField(default=None)
    end = models.DateField(default=None)

    #detail of a user who is currently logged in ...
    username = models.CharField(max_length=30)
    useremail = models.EmailField(max_length=50, default=None)
    userpassword = models.CharField(max_length=200)

    # details of the hotel for which user is currently doing the booking...
    hotelname = models.CharField(max_length=80, default=None)
    city = models.CharField(max_length=60, default=None)
    state = models.CharField(max_length=60, default=None)
    current_cost = models.FloatField(default=0.0)
    payment_status = models.CharField(max_length=50, default='Unpaid')


# this model is for any queries of customers.....
QUERY_CHOICE = (
    ('Pending', 'Pending'),
    ('Resolved', 'Resolved'),
)




class Query(models.Model):
    username = models.CharField(max_length=50)
    useremail = models.EmailField(max_length=50)
    contact_no = models.CharField(max_length=13)
    querydetails = models.TextField()
    date = models.DateField(default=date.today)
    querystatus = models.CharField(
        choices=QUERY_CHOICE, max_length=50, default='Pending'
    )

