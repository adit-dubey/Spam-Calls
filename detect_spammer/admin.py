from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DetectSpammer, Spam, Contact

@admin.register(DetectSpammer)
class DetectSpammerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')

@admin.register(Spam)
class SpamAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'reported_by')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'name')

