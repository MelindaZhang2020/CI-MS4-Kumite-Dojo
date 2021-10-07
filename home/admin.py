from django.contrib import admin
from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = ("alt_text", "image_tag")


admin.site.register(Banner, BannerAdmin)
