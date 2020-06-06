from django.db import models
from multiselectfield import MultiSelectField


class product(models.Model):

    COLORS = (
        ('blue', 'blue'),
        ('red', 'red'),
        ('yellow', 'yellow')
    )

    SIZE = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L')
    )


    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    colors = MultiSelectField(choices=COLORS)
    size = MultiSelectField(choices=SIZE)

    def __str__(self):
        return self.name