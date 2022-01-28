from django.db import models

# Create your models here.

class Todo(models.Model):
    team_name = models.CharField(max_length=200)
    team_captain = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.team_name
