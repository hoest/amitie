from django.db import models


PAGE_TYPE = (
  ("nieuws", "Nieuws"),
  ("agenda", "Agenda"),
  ("notule", "Notule"),
  ("menu", "Menu"),
  ("special", "Speciaal type (voor homepage e.d.)"),
  ("all", "Overig"),
)


class Page(models.Model):
  title = models.CharField(max_length=1024, verbose_name="Titel")
  page_type = models.CharField(max_length=256, verbose_name="Titel", choices=PAGE_TYPE, default="all")
  alias = models.SlugField(unique=False, blank=True, verbose_name="Technische alias")
  body = models.TextField(verbose_name="Tekst")
  created = models.DateTimeField(auto_now_add=True, verbose_name="Creatie datum")
  slug = models.SlugField(unique=True)

  def __unicode__(self):
    return self.title

  class Meta:
    """
    Meta shizzle
    """
    verbose_name = "pagina"
    verbose_name_plural = "pagina's"


class Picture(models.Model):
  page = models.ForeignKey(Page)
  picture = models.ImageField(upload_to="./pictures/", verbose_name="Afbeelding", help_text="Maximaal 280px breed", blank=True)

  class Meta:
    """
    Meta shizzle
    """
    verbose_name = "afbeelding"
    verbose_name_plural = "afbeeldingen"
