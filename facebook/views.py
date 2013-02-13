from django.http import HttpResponseRedirect
from django.shortcuts import render
from facebook.models import Person
from facebook.forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def index(request):
  search = request.GET.get("q", "")
  persons = Person.objects.all().order_by("lastname") if search == "" else Person.objects.filter(slug__icontains=search).order_by("lastname")
  paginator = Paginator(persons, 10)
  page = request.GET.get('page')

  try:
    persons = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    persons = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    persons = paginator.page(paginator.num_pages)

  context = {
    "search": search,
    "persons": persons,
    "next_birthday": Person.objects.get_birthday(4)
  }

  return render(request, "facebook.html", context)


@login_required
def person_by_slug(request, slug):
  context = {
    "person": Person.objects.get(slug=slug),
  }

  return render(request, "person.html", context)


def person_login(request):
  next = request.GET.get("next", "/")

  if request.user.is_authenticated():
    return HttpResponseRedirect("/")
  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data["username"]
      password = form.cleaned_data["password"]
      person = authenticate(username=username, password=password)
      if person is not None:
        login(request, person)
        return HttpResponseRedirect(next)
      else:
        return render(request, "login.html", {"form": form})
    else:
      return render(request, "login.html", {"form": form})
  else:
    context = {
      "form": LoginForm()
    }

    return render(request, "login.html", context)


def person_logout(request):
  logout(request)
  return HttpResponseRedirect("/login/")
