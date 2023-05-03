from django.contrib import admin
from .models import ArticleCache


# Register your models here.
@admin.register(ArticleCache)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    ArticleCache._meta.get_fields()]