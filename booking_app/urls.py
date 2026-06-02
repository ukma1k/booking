from django.urls import path
from booking_app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('booking/<int:apartment_id>/', views.booking_page, name='booking_page'),
]
