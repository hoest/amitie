from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns("",
    url(r"^$", views.index, name="index"),
    url(r"^tag/(?P<page_type>.*)/$", views.index_by_type, name="page_type"),
    url(r"^(?P<slug>.*)/$", views.page_by_slug, name="page_by_slug"),
)
