from django.db import models


class Person(models.Model):
  """
  Person class
  """
  lastname = models.CharField(max_length=256, verbose_name="Achternaam")
  initials = models.CharField(max_length=256, verbose_name="Initialen")
  firstname = models.CharField(max_length=256, verbose_name="Voornaam")
  street = models.CharField(max_length=256, verbose_name="Straat en huisnummer")
  zipcode = models.CharField(max_length=6, verbose_name="Postcode")
  city = models.CharField(max_length=256, verbose_name="Plaats")
  date_of_birth = models.DateField(verbose_name="Geboortedatum")
  picture = models.ImageField(upload_to="pictures/", verbose_name="Foto")
  member_since = models.DateField(verbose_name="Lid sinds")
  phonenumber = models.CharField(max_length=12, verbose_name="Telefoonnummer")
  cellphone = models.CharField(max_length=12, verbose_name="Mobiel")
  pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publicatie datum")

  def __unicode__(self):
    return "{0}, {1}".format(unicode(self.lastname, "utf-8"), unicode(self.initials, "utf-8"))

  class Meta:
    verbose_name = "persoon"
    verbose_name_plural = "personen"
