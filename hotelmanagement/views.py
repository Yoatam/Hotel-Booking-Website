

from django.shortcuts import render, redirect
from .models import Hotel
from .forms import HotelForm

# Create your views here.
def hotel_management(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('login')  # Redirect non-admin users to login page

    hotels = Hotel.objects.all()
    return render(request, 'hotel_management.html', {'hotels': hotels})

def add_hotel(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel_management')
    else:
        form = HotelForm()
    return render(request, 'add_hotel.html', {'form': form})

def edit_hotel(request, hotel_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('login')

    hotel = Hotel.objects.get(id=hotel_id)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotel_management')
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'edit_hotel.html', {'form': form})

def delete_hotel(request, hotel_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('login')

    hotel = Hotel.objects.get(id=hotel_id)
    if request.method == 'POST':
        hotel.delete()
        return redirect('hotel_management')
    return render(request, 'delete_hotel.html', {'hotel': hotel})


