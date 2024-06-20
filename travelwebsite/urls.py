"""
URL configuration for travelwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mainapp import views as v1
from bookings import views as v2
from hotellist import views as v3
from travelwebsite import views as v4
from userreview import views as v5
from payments import views as v6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v4.homepage, name='home'),
    path('<id>', v4.homepage, name='home'),
    path('about/', v4.about, name='about'),
    path('about/<id>', v4.about, name='about'),
    path('services/', v4.services, name='service'),
    path('services/<id>', v4.services, name='service'),
    path('pricings/', v4.price, name='price'),
    path('blogs/', v5.blog, name='blog'),
    path('blogs/<id>', v5.blog, name='blog'),
    path('review/<id>', v5.review, name='review'),
    path('memories/<id>', v5.memory, name='memory'),
    path('dashboard/<id>', v2.dashboard, name='dashboard'),
    path('bookings/<id>/', v2.bookings, name='booking'),
    path('dashboard/deleteConfirmation/', v2.delete_confirmation, name='delete'),
    path('dashboard/deleteConfirmation/delete/', v2.delete, name='delete'),
    path('quaries/<id>', v2.query, name='query'),
    path('details/', v2.details, name='order_details'),
    path('login/', v1.login, name='login'),
    path('login/<id>', v1.login, name='login'),
    # this is for update the password before login..
    path('update/', v1.update, name='update'),
    path('signup/', v1.signup, name='signup'),
    path('hotellist/<hotelstate>/<id>', v3.hotellist, name='hotellist'),
    path('payments/', v6.paymentpage, name='payment'),
    path('logout/<id>/', v1.logout_user, name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
