from django.db import models
from django.core.validators import MaxValueValidator

# create models that shown for each single movie by using django fields
class Movie(models.Model):
    name = models.CharField(max_length=200)
    picture = models.URLField(max_length=900, default='https://via.placeholder.com/300x400?text=No+photo')
    # use PositiveIntegerField to just accept positive numbers, and validators=[MaxValueValidator(10)] to set the max up to 10 by use array from django
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    notes = models.TextField(max_length=2000, default='')
    # use the str method to display it very friendly with the database
    def __str__(self):
        return self.name

# after we finish create our model we need to provide it with url and view to see it and edit it
# create urls file by move courser to movies in left side >> right click, new >> python file >> name it urls
