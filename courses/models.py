from django.db import models
from django.http import Http404


class BaseModel(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def get_or_fail_by_pk(cls, pk):
        try:
            return cls.objects.get(pk=pk)
        except Exception as e:
            raise Http404('Not Excist')


class Course(BaseModel):
    title = models.CharField(max_length=100)
    icon_address = models.CharField(max_length=256, null=True, blank=True)
    relative_address = models.CharField(max_length=256, null=True, blank=True)
    number_in_row = models.IntegerField(default=1)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.id:
            super(Course, self).save()
            self.relative_address = 'api/' + str(self.id) + '/lessons/'
        super(Course, self).save()


class Lesson(BaseModel):
    course = models.ForeignKey('Course', related_name='lessons', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    relative_address = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.title

    def save(self):
        if not self.id:
            super(Lesson, self).save()
            self.relative_address = 'api/' + str(self.id) + '/parts/'
        super(Lesson, self).save()


class Part(BaseModel):
    ICON_CHOICES = [('md-play', 'Reading'), ('md-help', 'Question')]
    lesson = models.ForeignKey('Lesson', related_name='parts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    icon = models.CharField(choices=ICON_CHOICES, max_length=50, default=1)
    text = models.TextField()

    def __str__(self):
        return self.title
