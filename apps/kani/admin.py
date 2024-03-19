from django.contrib import admin
from django.contrib.auth.models import User, Group

# Register your models here.\
from apps.kani.models import InfoUser, Secondary

admin.site.register(InfoUser)

admin.site.register(Secondary)

admin.site.unregister(User)
admin.site.unregister(Group)

