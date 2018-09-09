from django.db import models
from django.utils import timezone

# Create your models here.

class CourseGrades(models.Model):
    courseTypeChoices = ( ("General" , "general") , ('Basic' , 'basic') , ("Profesional" , 'profesional') ,)
    departments = (("Mathematics department" , "Mathematics department") ,
     ("Computer Engineering department","Computer Engineering department"),
    ("Chemistry and Petroleum Engineering","Chemistry and Petroleum Engineering") ,
     ("Religous Center","Religous Center") , ("Language Center","Language Center") ,)
    CourseName = models.CharField(max_length = 32)
    UnitsNumber = models.SmallIntegerField()
    Type = models.CharField(max_length = 32 , choices = courseTypeChoices , default = "Profesional")
    Department = models.CharField(max_length = 56 , choices = departments , default = "Mathematics department")
    Grade = models.SmallIntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.CourseName

    class Meta:
        ordering = ('-date',)

class Post(models.Model):
    Title = models.CharField(max_length = 255)
    Author = models.CharField(max_length = 255)
    Body = models.TextField()
    date = models.DateField(default=timezone.now)
