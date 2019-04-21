from django.db import models
#from multiselectfield import MultiSelectField

#TodoItem class
class TodoItem(models.Model):
    content = models.TextField()
    #Tasks are not completed by default
    completed = models.BooleanField(default=False)
    
    def __str__(self):
      return self.content