from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'

class City_m(models.Model):
    name = models.CharField(max_length=50)
    wiki_link= models.URLField()
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)

    def __str__(self):
        return self.name

    def __rep__(self):
        return self.name + " " + str(self.latitude) + " " + \
            str(self.longitude) + " " +self.wiki_link
