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
            raise Http404('Not Exist')


def course_icon_directory(self, filename):
    return 'course_icon/{0}'.format(filename)


class School(BaseModel):
    title = models.CharField(max_length=100, null=True, default=None)
    relative_address = models.CharField(max_length=256, null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title


class Course(BaseModel):
    SORT_CHOICES = [(1, 'Alone'), (2, 'With other'), (3, 'With 2 other')]
    school = models.ForeignKey('School', related_name='courses', on_delete=models.CASCADE, null=True, default=None)
    title = models.CharField(max_length=100)
    icon_address = models.CharField(max_length=256, null=True, blank=True)
    relative_address = models.CharField(max_length=256, null=True, blank=True)
    number_in_row = models.IntegerField(choices=SORT_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True, null=True)
    order_id = models.IntegerField(default=0, blank=False, null=False)
    icon = models.ImageField(upload_to=course_icon_directory, null=True)

    class Meta(object):
        ordering = ('order_id',)

    def __str__(self):
        return self.title

    __original_icon = None
    # __original_order_id = None

    def __init__(self, *args, **kwargs):
        super(Course, self).__init__(*args, **kwargs)
        self.__original_icon = self.icon
        # self.__original_order_id = self.order_id

    def save(self):
        # if self.order_id != self.__original_order_id:
        #     super(Course, self).save()
        if not self.pk:
            super(Course, self).save()
        self.relative_address = '/api/courses/' + str(self.pk)
        if self.icon != self.__original_icon:
            super(Course, self).save()
            self.icon_address = self.icon.url
        super(Course, self).save()
        self.__original_icon = self.icon
        # self.__original_order_id = self.order_id


class Lesson(BaseModel):
    course = models.ForeignKey('Course', related_name='lessons', on_delete=models.CASCADE, null=True)
    # school = models.ForeignKey('School', related_name='lessons_school', on_delete=models.CASCADE, null=True, default=None)
    title = models.CharField(max_length=100)
    relative_address = models.CharField(max_length=256, blank=True)
    order_id = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order_id',)

    def __str__(self):
        return self.title

    def save(self):
        if not self.pk:
            # related_lessons = Lesson.objects.filter(course=self.course)
            # last_lesson = related_lessons.order_by('-order_id')[0]
            # self.order_id = last_lesson.order_id + 1
            super(Lesson, self).save()
            self.relative_address = '/api/lessons/' + str(self.pk)
        # course = Course.objects.get(pk=self.course.pk)
        # self.school = course.school
        super(Lesson, self).save()

    @property
    def school(self):
        return self.course.school


class Part(BaseModel):
    # ICON_CHOICES = [('md-arrow-dropleft', 'Reading'), ('md-help-buoy', 'Question')]
    ICON_CHOICES = [('md-play', 'Reading'), ('md-help', 'Question')]
    lesson = models.ForeignKey('Lesson', related_name='parts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    icon = models.CharField(choices=ICON_CHOICES, max_length=50, default=1)
    text = models.TextField(null=True)
    order_id = models.IntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order_id',)

    def __str__(self):
        return self.title

    # def save(self):
    #     if not self.pk:
    #         related_parts = Part.objects.filter(lesson=self.lesson)
    #         last_part = related_parts.order_by('-order_id')[0]
    #         self.order_id = last_part.order_id + 1
    #         super(Part, self).save()
    #     super(Part, self).save()