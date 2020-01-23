from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 60)
    description = models.TextField()
    technology = models.CharField(max_length = 20)
    image= models.ImageField(blank = False)
    giturl = models.TextField(max_length = 200 )
    live = models.TextField(max_length = 200)

    
    
@classmethod
def get_all_projects(cls):
        images = cls.objects.all()
        return images
    