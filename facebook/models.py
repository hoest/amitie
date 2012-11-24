from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class PersonManager(models.Manager):
  """
  PersonManager class
  """
  def get_birthday(self, nweeks):
    now = datetime.today()
    persons = self.all().extra(select={
      "sortday": "EXTRACT(DAY FROM date_of_birth)",
      "sortmonth": "EXTRACT(MONTH FROM date_of_birth)"
    }, order_by=["sortmonth", "sortday"])

    result = []
    for p in persons:
      if(nweeks >= 0):
        for i in range(0, abs(nweeks) * 7):
          cday = now + timedelta(days=i)
          if p.has_birthday(cday):
            result.append(p)
      else:
        for i in range(1, abs(nweeks) * 7):
          cday = now - timedelta(days=i)
          if p.has_birthday(cday):
            result.append(p)

    return result


class Person(models.Model):
  """
  Person class
  """
  objects = PersonManager()

  user = models.OneToOneField(User)
  lastname = models.CharField(max_length=256, verbose_name="Achternaam")
  initials = models.CharField(max_length=256, verbose_name="Voorletters")
  firstname = models.CharField(max_length=256, verbose_name="Voornaam")
  street = models.CharField(max_length=256, verbose_name="Straat en huisnummer")
  zipcode = models.CharField(max_length=6, verbose_name="Postcode")
  city = models.CharField(max_length=256, verbose_name="Plaats")
  date_of_birth = models.DateField(verbose_name="Geboortedatum")
  picture = models.ImageField(upload_to="./pictures/", verbose_name="Foto", help_text="Maximaal 250px breed", blank=True)
  member_since = models.DateField(verbose_name="Lid sinds")
  phonenumber = models.CharField(max_length=12, verbose_name="Telefoonnummer")
  cellphone = models.CharField(max_length=12, verbose_name="Mobiel", blank=True)
  email = models.CharField(max_length=256, verbose_name="Emailadres", blank=True)
  pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publicatie datum")
  slug = models.SlugField(unique=True)

  def has_birthday(self, current_day):
    return current_day.day == self.date_of_birth.day and current_day.month == self.date_of_birth.month

  def __unicode__(self):
    """
    String represetation of a person object
    """
    return u"%s, %s" % (self.lastname, self.firstname)

  class Meta:
    """
    Meta shizzle
    """
    verbose_name = "persoon"
    verbose_name_plural = "personen"
