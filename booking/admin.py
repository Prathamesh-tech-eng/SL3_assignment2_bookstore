from django.contrib import admin

# Register your models here.
# booking/admin.py
from django.contrib import admin
from .models import Show, Booking

admin.site.register(Show)
admin.site.register(Booking)
