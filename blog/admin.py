from django.contrib import admin
from .models import CourseGrade , Post

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('CourseName','Grade' , 'UnitsNumber', 'Type', 'Department',)
    search_fields = ('CourseName', 'UnitsNumber' , 'TermNumber')
    list_filter = ('TermNumber','Type','Department')
    prepopulated_fields = {'CourseName': ('Department',)}
    date_hierarchy = 'date'
    ordering = ['TermNumber' , 'Grade' , 'Type']
class PostAdmin(admin.ModelAdmin):
    list_display = ('Title' , 'Author')

admin.site.register(CourseGrade , CourseAdmin);
admin.site.register(Post , PostAdmin);
