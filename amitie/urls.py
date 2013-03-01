from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import os

SITE_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

urlpatterns = patterns("",
  # Examples:
  # url(r"^$", "amitie.views.home", name="home"),
  # url(r"^amitie/", include("amitie.foo.urls")),

  url(r"^$", "pages.views.home", name="home"),

  url(r"^login/", "facebook.views.person_login", name="login"),
  url(r"^logout/", "facebook.views.person_logout", name="logout"),
  url(r'^accounts/', include('django.contrib.auth.urls')),
  url(r"^leden/", include("facebook.urls")),

  url(r"^pages/", include("pages.urls")),

  url(r"^admin/doc/", include("django.contrib.admindocs.urls")),
  url(r"^admin/", include(admin.site.urls)),

  (r"^static/admin/css/(?P<path>.*)$", "django.views.static.serve", {"document_root": os.path.join(SITE_ROOT, "static/admin/css")}),
  (r"^static/admin/img/(?P<path>.*)$", "django.views.static.serve", {"document_root": os.path.join(SITE_ROOT, "static/admin/img")}),
  (r"^static/admin/js/(?P<path>.*)$", "django.views.static.serve", {"document_root": os.path.join(SITE_ROOT, "static/admin/js")}),

  (r"^css/(?P<path>.*)$", "django.views.static.serve", {"document_root": os.path.join(SITE_ROOT, "static/css")}),
  (r"^js/(?P<path>.*)$", "django.views.static.serve", {"document_root": os.path.join(SITE_ROOT, "static/js")}),
  (r"^images/(?P<path>.*)$", "django.views.static.serve", {"document_root": os.path.join(SITE_ROOT, "static/images")}),
  (r"^media/pictures/(?P<path>.*)$", "django.views.static.serve", {"document_root": os.path.join(SITE_ROOT, "media/pictures")}),
  (r"^media/cache/(?P<path>.*)$", "django.views.static.serve", {"document_root": os.path.join(SITE_ROOT, "media/cache")}),
)
