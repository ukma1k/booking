from django.shortcuts import render
from booking_app.models import Category, Apartments, Booking
def home(request):
    apartments = Apartments.objects.all()
    return render(request, 'index.html', {"name": "Booking App", "apartments": apartments})


def booking_page(request, apartment_id):

    apartment = Apartments.objects.get(id=apartment_id)
    context = {"apartment": apartment}
    
    return render(request, 'booking.html', context)