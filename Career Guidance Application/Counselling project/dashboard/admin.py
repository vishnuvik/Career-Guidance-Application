from django.contrib import admin
from .models import Data

# Register your models here.


class DataAdmin(admin.ModelAdmin):
    list_display = ('Rank','India','Ethiopia','Nepal','Tenth','Twelth','predictions')


admin.site.register(Data, DataAdmin)
