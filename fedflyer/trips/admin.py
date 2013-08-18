from .models import *
from django.contrib import admin

class DestinationInline(admin.TabularInline):
    model = Destination

class ExpenseInline(admin.TabularInline):
    model = Expense

class TripAdmin(admin.ModelAdmin):
    inlines = [
        DestinationInline,
        ExpenseInline
    ]

    
admin.site.register(Trip, TripAdmin)
