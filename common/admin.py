from django.contrib import admin

from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site



admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)