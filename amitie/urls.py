from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
  # Examples:
  # url(r"^$", "amitie.views.home", name="home"),
  # url(r"^amitie/", include("amitie.foo.urls")),

  url(r"^login/", "facebook.views.person_login", name="login"),
  url(r"^logout/", "facebook.views.person_logout", name="logout"),
  url(r"^leden/", include("facebook.urls")),

  url(r"^admin/doc/", include("django.contrib.admindocs.urls")),
  url(r"^admin/", include(admin.site.urls)),
  (r"^css/(?P<path>.*)$", "django.views.static.serve", {"document_root": "./static/css"}),
  (r"^js/(?P<path>.*)$", "django.views.static.serve", {"document_root": "./static/js"}),
  (r"^images/(?P<path>.*)$", "django.views.static.serve", {"document_root": "./static/images"}),
  (r"^pictures/(?P<path>.*)$", "django.views.static.serve", {"document_root": "./pictures"}),
)
