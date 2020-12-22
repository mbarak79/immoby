from django.contrib import admin
from .models import FeaturedProperties, Property_types, Property_status

# Register your models here.

admin.site.register(FeaturedProperties)
admin.site.register(Property_types)
admin.site.register(Property_status)