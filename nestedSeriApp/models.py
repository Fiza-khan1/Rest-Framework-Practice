from django.db import models


class GFG(models.Model): 
    name = models.CharField(max_length=100) 
    def __str__(self):
        return self.name
  
class Item(models.Model): 
    gfg = models.ForeignKey(GFG, on_delete=models.CASCADE) 
    item_title = models.CharField(max_length=100) 
    def __str__(self):
        return self.item_title


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username
    
