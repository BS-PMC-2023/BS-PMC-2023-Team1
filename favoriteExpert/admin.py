from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import favoriteExpert


# Register your models here.
@admin.register(favoriteExpert)
class RequestDemoAdmin2(admin.ModelAdmin):
    list_display = [field.name for field in
                    favoriteExpert._meta.get_fields()]
