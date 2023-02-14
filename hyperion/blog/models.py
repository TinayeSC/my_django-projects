from django.db import models
# Create your models here.
class Post(models.Model):
   """This class defines the different aspects of the blog class.
   
   :param title: The title of the blog post displayed at the top of the page
   :type title: str, required
   :param body: The body/content of the blog post.
   :type body: str, required
   :param works_cited: This is the field that includes the sources used
      in the blog post. This will be displayed at the end of the body; will
      display "No works cited" if no sources were used in the post.
   :type works_cited: str,optional 
   :param by_line: The by line simply displays who the blog post was authored by
   :type by_line: str,fixed
   :param signature: This displays a closing signature beneath the by line.
   :type signature: str, fixed
   :param date: This is the date that the blog post was written, which will 
      be displayed at the top
   :type date: date, required 
   """
   # Default behaviour - Django creates primary keys for you
   title = models.CharField(max_length=140)
   body = models.TextField()
   works_cited = models.TextField(default = "No Works Cited")
   by_line = """ Written by TSC."""
   signature = """'Enough turbulent meaninglessness creates purpose' - Cixin Liu"""
   date = models.DateTimeField()
  
def __str__(self):
   """This method returns the title from one of the blog class objects"""
   return self.title