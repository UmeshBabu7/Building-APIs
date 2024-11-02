from django.contrib import admin
from .models import Category,MenuItem

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory', 'category')
    
