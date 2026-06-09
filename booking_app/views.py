from django.shortcuts import render, redirect
from booking_app.models import Category, Apartments, Booking
def home(request):
    apartments = Apartments.objects.all()
    return render(request, 'index.html', {"name": "Booking App", "apartments": apartments})


def booking_page(request, apartment_id):

    apartment = Apartments.objects.get(id=apartment_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        booking = Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            apartment=apartment,
            check_in=check_in,
            check_out=check_out
        )

        return redirect('confirmation', booking_id=booking.id)

    context = {"apartment": apartment}
    
    return render(request, 'booking.html', context)

def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    apartment = booking.apartment
    return render(request, 'booking_con.html', {'booking': booking, 'apart': apartment})