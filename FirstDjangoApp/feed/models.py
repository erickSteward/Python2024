from django.db import models

# Create your models here.
class Posts(models.Model):
    text =models.CharField(max_length=140, blank=False, null=False)
    
def __string__(self):
    return self.text
