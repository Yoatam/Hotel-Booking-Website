from django.contrib import admin
from django.contrib.admin.sites import site
from bookings.models import Bookinghotel, Query

# Register your models here.
class BookinghotelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "firstname",
        "lastname",
        "email",
        "contact_no",
        "no_people",
        "no_rooms",
        "start",
        "end",
        "hotelname",
        "city",
        "state",
        "current_cost",
        "payment_status",
        "username",
        "useremail",
        "userpassword",
    )


class QueryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "useremail",
        "contact_no",
        "querydetails",
        "date",
        "querystatus",
    )


admin.site.register(Bookinghotel, BookinghotelAdmin)
admin.site.register(Query, QueryAdmin)