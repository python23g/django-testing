from django.db import models


class Animal(models.Model):
   name = models.CharField(max_length=30)
   sound = models.CharField(max_length=50)

   def speak(self):
       return f'The {self.name} says "{self.sound}"'

   def __str__(self):
       return self.name

