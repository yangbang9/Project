from django.contrib import admin
from background_setting.models import offensive, defensive
# Register your models here.

class OptionAdmin(admin.ModelAdmin):
    fields = ['number']
    # fieldsets = [
    #     ('INFORMATION', {'fields':['name']}),
    #     ('OTHER', {'fields':['age']}) 
    # ]
# admin.site.register(Option, OptionAdmin)