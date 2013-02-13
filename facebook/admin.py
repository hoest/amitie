from facebook.models import Person
from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("firstname", "lastname")}
  ordering = ("lastname", "firstname")

admin.site.register(Person, PersonAdmin)
