import imp
from msilib.schema import ServiceInstall
from urllib import request
from django.contrib import admin
from .models import Review

# Register your models here.
admin.site.register(Review)