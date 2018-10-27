from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actusl city name on the dashboard
        return self.name

    class Meta: #show the plural of city os cities instead of citys
        verbose_name_plural = 'cities'