from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=225, blank = True, null = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"my text is:{self.text}"