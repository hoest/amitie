from django.conf.urls import patterns, url

from facebook import views

urlpatterns = patterns("",
    url(r"^$", views.index, name="index"),
    url(r"^(?P<slug>.*)/$", views.person_by_slug, name="person_by_slug"),
)
