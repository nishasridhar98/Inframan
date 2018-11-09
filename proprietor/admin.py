from django.contrib import admin
from proprietor.models import Property,Profile,Tenant

# Register your models here.
admin.site.register(Property)
admin.site.register(Profile)
admin.site.register(Tenant)