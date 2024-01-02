from django.db import models
from .views import signup
# Create your models here.
class signup(models.Model):
    user_name = models.CharField(max_length = 100)
    # domain = models.CharField(max_length = 100)
    # company = models.CharField(max_length = 100)
