from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Locations)
admin.site.register(Areas)
admin.site.register(Boulders)
admin.site.register(Climbs)