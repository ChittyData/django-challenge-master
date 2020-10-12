#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Company, Contact, Order

# Register your models here.
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Order)