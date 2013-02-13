from pages.models import Page, Picture
from django.contrib import admin


class PicturesInline(admin.TabularInline):
  model = Picture


class PageAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title", )}
  ordering = ("-created", "title")
  inlines = [
    PicturesInline,
  ]

admin.site.register(Page, PageAdmin)
