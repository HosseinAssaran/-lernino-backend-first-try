from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    iconAddr = models.CharField(max_length=256)
    relAddr = models.CharField(max_length=256)
    numInRow = models.IntegerField(null=True)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey('Course', related_name='lessons', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    relAddr = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Page(models.Model):
    lesson = models.ForeignKey('Lesson', related_name='pages', on_delete=models.CASCADE, null=True)
    key = models.CharField(max_length=100)
    icon = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return self.title    
    