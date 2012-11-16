from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
  """
  Person class
  """
  user = models.OneToOneField(User)
  lastname = models.CharField(max_length=256, verbose_name="Achternaam")
  initials = models.CharField(max_length=256, verbose_name="Initialen", blank=True)
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

  def __unicode__(self):
    """
    String represetation of a person object
    """
    return u"%s, %s " % (self.lastname, self.firstname)

  class Meta:
    """
    Meta shizzle
    """
    verbose_name = "persoon"
    verbose_name_plural = "personen"
