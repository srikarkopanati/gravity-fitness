from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.timezone import localtime
from django.http import HttpResponseNotAllowed
from .models import FitnessClass, Booking
from django.contrib.auth.decorators import login_required


def index(request):
    classes = FitnessClass.objects.all()[:3]  # Get 3 classes for preview
    return render(request, 'index.html', {'classes': classes})

def class_list(request):
    class_type = request.GET.get('class_type', '')
    if class_type:
        classes = FitnessClass.objects.filter(name=class_type)
    else:
        classes = FitnessClass.objects.all()
    return render(request, 'classes.html', {'classes': classes, 'class_types': FitnessClass.CLASS_TYPES})

# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'login.html')

# Registration view
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')

    return render(request, 'register.html')

# Home page with intro
def home(request):
    return render(request, 'home.html')

# Classes listing
def classes(request):
    classes = FitnessClass.objects.all().order_by('datetime')
    user_bookings = Booking.objects.filter(user=request.user).values_list('fitness_class_id', flat=True)
    return render(request, 'classes.html', {'classes': classes, 'user_bookings': user_bookings})

# Booking form page (GET) and booking confirmation (POST)
from django.shortcuts import render, get_object_or_404, redirect
from .models import FitnessClass, Booking


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import FitnessClass, Booking

@login_required
def book_class(request, class_id):
    fitness_class = get_object_or_404(FitnessClass, id=class_id)

    if request.method == 'GET':
        already_booked = Booking.objects.filter(user=request.user, fitness_class=fitness_class).exists()
        return render(request, 'booking.html', {
            'fitness_class': fitness_class,
            'already_booked': already_booked
        })

    # POST request
    if Booking.objects.filter(user=request.user, fitness_class=fitness_class).exists():
        return render(request, 'booking.html', {
            'fitness_class': fitness_class,
            'message': '✅ You have already booked this class.',
            'already_booked': True
        })

    if fitness_class.available_slots <= 0:
        return render(request, 'booking.html', {
            'fitness_class': fitness_class,
            'message': '❌ Sorry, no slots available.',
            'already_booked': False
        })

    # Proceed to book
    phone = request.POST.get('phone')
    Booking.objects.create(
        fitness_class=fitness_class,
        user=request.user,
        phone=phone
    )
    fitness_class.available_slots -= 1
    fitness_class.save()

    return render(request, 'booking.html', {
        'fitness_class': fitness_class,
        'message': '✅ Booking confirmed!',
        'already_booked': True
    })

# Show bookings
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})


def logout_confirm(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout_confirm.html')

from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')
