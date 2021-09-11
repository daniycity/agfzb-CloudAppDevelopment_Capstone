from django.contrib import admin
from .models import CarModel, CarMake 


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 3
    
    

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Type', 'Year', 'DealerId')
    
    

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('Name', 'Description', 'Slogan')
    
    

# Register models here
admin.site.register(CarModel)
admin.site.register(CarMake)
