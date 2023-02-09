from django.db import models
# Create your models here.
class Post(models.Model):
   # Default behaviour - Django creates primary keys for you
   title = models.CharField(max_length=140)
   body = models.TextField()
   works_cited = models.TextField(default = "No Works Cited")
   by_line = """ Written by TSC."""
   signature = """'Enough turbulent meaninglessness creates purpose' - Cixin Liu"""
   date = models.DateTimeField()
  
def __str__(self):
   return self.title