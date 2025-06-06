from django.contrib import admin
from .models import Booking, FitnessClass

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('fitness_class', 'user', 'phone')
    search_fields = ('user__username', 'phone', 'fitness_class__name')
    list_filter = ('fitness_class__name',)
    ordering = ('fitness_class',)

@admin.register(FitnessClass)
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor', 'datetime', 'available_slots')
    search_fields = ('name', 'instructor')
