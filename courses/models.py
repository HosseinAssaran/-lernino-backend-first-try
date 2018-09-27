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


class Course(BaseModel):
    SORT_CHOICES = [(1, 'Alone'), (2, 'With other'), (3, 'With 2 other')]
    title = models.CharField(max_length=100)
    icon_address = models.CharField(max_length=256, null=True, blank=True)
    relative_address = models.CharField(max_length=256, null=True, blank=True)
    number_in_row = models.IntegerField(choices=SORT_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True, null=True)
    order_id = models.IntegerField(default=0, unique=True)
    icon = models.ImageField(upload_to=course_icon_directory, null=True)

    class Meta:
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
        self.relative_address = '/api/' + str(self.order_id) + '/lessons/'
        if self.icon != self.__original_icon:
            super(Course, self).save()
            self.icon_address = self.icon.url
        super(Course, self).save()
        self.__original_icon = self.icon
        # self.__original_order_id = self.order_id


class Lesson(BaseModel):
    course = models.ForeignKey('Course', related_name='lessons', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    relative_address = models.CharField(max_length=256, blank=True)
    order_id = models.IntegerField(default=0, unique=True)

    class Meta:
        ordering = ('order_id',)

    def __str__(self):
        return self.title

    def save(self):
        # if not self.id:
        #     super(Lesson, self).save()
        self.relative_address = '/api/' + str(self.order_id) + '/parts/'
        super(Lesson, self).save()


class Part(BaseModel):
    ICON_CHOICES = [('md-arrow-dropleft', 'Reading'), ('md-help-buoy', 'Question')]
    lesson = models.ForeignKey('Lesson', related_name='parts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    icon = models.CharField(choices=ICON_CHOICES, max_length=50, default=1)
    text = models.TextField(null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title
