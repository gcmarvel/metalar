from django.contrib import admin

from .models import Service, ServiceImage


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage


class ServiceAdmin(admin.ModelAdmin):
    model = Service
    inlines = [
        ServiceImageInline
    ]


admin.site.register(Service, ServiceAdmin)
