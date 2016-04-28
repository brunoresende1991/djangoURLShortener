from django.db import models
from django.core.urlresolvers import reverse
from .basechanger import decimal2base_n, base_n2decimal

# Create your models here.
class Urls(models.Model):
    short_id = models.SlugField(max_length=6,primary_key=True)
    httpurl = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
 
    def __str__(self):
        return self.httpurl

class Link (models.Model):
    url = models.URLField()

    def encurtar(link):
        l, _ = Link.objects.get_or_create(url=link.url)
        return str(decimal2base_n(l.pk))

    def expandir(slug):
        link_id = int(base_n2decimal(slug))
        l = Link.objects.get(pk=link_id)
        return l.url

    def get_absolute_url(self):
        return reverse("shortenurl", kwargs={"pk": self.pk})

    def url_curta(self):
        return reverse("redirectoriginal", kwargs={"short_id": Link.encurtar(self)})
