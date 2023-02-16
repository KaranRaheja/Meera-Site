from django.contrib import admin
from .models import Activity
from .models import Food
from .models import Drink



# Register your models here.

admin.site.register(Activity)
admin.site.register(Food)
admin.site.register(Drink)