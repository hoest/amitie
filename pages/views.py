from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from facebook.models import Person
from pages.models import Page


@login_required
def index(request):
  context = {
    "pages": Page.objects.exclude(page_type="special").order_by("-created"),
  }

  return render(request, "index.html", context)


@login_required
def index_by_type(request, page_type):
  context = {
    "pages": Page.objects.filter(page_type=page_type).order_by("-created"),
    "tag": page_type
  }

  return render(request, "index.html", context)


@login_required
def page_by_slug(request, slug):
  context = {
    "page": Page.objects.get(slug=slug),
  }

  return render(request, "page.html", context)


@login_required
def home(request):
  context = {
    "page": Page.objects.get(alias="home"),
    "next_birthday": Person.objects.get_birthday(4),
    "nieuws": Page.objects.filter(page_type="nieuws").order_by("-created")[0],
  }

  return render(request, "page.html", context)
