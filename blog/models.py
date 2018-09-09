from django.db import models
from django.utils import timezone

# Create your models here.

class CourseGrades(models.Model):
    courseTypeChoices = ("General" , "Basic" , "Profesional")
    department = ("Mathematics department" , "Computer Engineering department",
    "Chemistry and Petroleum Engineering" , "Religous Center" , "Language Center")
    CourseName = models.CharField(max_length = 32)
    UnitsNumber = models.SmallIntegerField()
    Grade = models.SmallIntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.CourseName

    class Meta:
        ordering = ('-date',)
