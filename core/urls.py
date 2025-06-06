from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('login/', views.user_login, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Registration page
    path('home/', views.home, name='home'),  # Intro page after login
    path('classes/', views.classes, name='classes'),  # List of all fitness classes
    path('book/<int:class_id>/', views.book_class, name='book_class'),  # Booking form page
    # path('book/<int:class_id>/', views.book_class, name='book_class'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),  # Show all bookings for current user
    path('logout_confirm/', views.logout_confirm, name='logout_confirm'),

]
