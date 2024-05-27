from django.contrib import admin
from create_supermarket.models import CreateSupermarket

# Register your models here.
@admin.register(CreateSupermarket)
class CreateSupermarketAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'supermarket']