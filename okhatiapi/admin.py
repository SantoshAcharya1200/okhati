from django.contrib import admin
from .models import OpeningHours,ExceptionDay

# Register your models here.

my_models=[OpeningHours,ExceptionDay]
admin.site.register(my_models)