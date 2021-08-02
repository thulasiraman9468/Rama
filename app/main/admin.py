from django.contrib import admin

# Register your models here.
from .models import booking

class bookingAdmin(admin.ModelAdmin):
    class Meta:
        model = booking
admin.site.register(booking, bookingAdmin)