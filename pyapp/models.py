from django.db import models


class Toy(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.name
