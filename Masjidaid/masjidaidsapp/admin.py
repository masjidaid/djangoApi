from django.contrib import admin

from .models import User, Masjid, MasjidsImages
# Register your models here.

admin.site.register(User)
admin.site.register(Masjid)
admin.site.register(MasjidsImages)