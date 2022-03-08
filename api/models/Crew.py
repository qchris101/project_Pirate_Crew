from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Crew(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  name = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The crew is named: '{self.name}'"

  def as_dict(self):
    """Returns dictionary version of Crew models"""
    return {
        'id': self.id,
        'name': self.name,
    }
