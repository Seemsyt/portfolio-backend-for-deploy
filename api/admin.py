import random
from django.contrib import admin
from .models import Contact, Pricing,Project
# Register your models here.
class PricingAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title','price','is_admin')
admin.site.register(Pricing,PricingAdmin)
admin.site.register(Contact)
admin.site.register(Project)