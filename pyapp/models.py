from django.db import Models


class Toy(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name
