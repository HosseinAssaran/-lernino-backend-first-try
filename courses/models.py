from django.db import models
from django.http import Http404
from django.conf import settings
import os


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
    if not self.pk:
        icon_id = None
    else:
        icon_id = self.pk
    return 'course_icon/IcnC{0}_{1}'.format(icon_id, filename)


def parts_image(self, filename):
    if not self.pk:
        image_id = None
    else:
        image_id = self.pk
    return 'parts_image/ImgL{0}_{1}'.format(image_id, filename)


class School(BaseModel):
    title = models.CharField(max_length=100, null=True, default=None)
    slug = models.CharField(max_length=10, null=True, default=None)
    relative_address = models.CharField(max_length=256, null=True, blank=True, default=None)
    app_last_version = models.CharField(max_length=256, null=True, blank=True, default=None)
    app_support_version = models.CharField(max_length=256, null=True, blank=True, default=None)
    app_address = models.CharField(max_length=256, null=True, blank=True, default=None)
    app_update_message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    order_id = models.IntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('order_id',)

    def __str__(self):
        return self.title

    def save(self):
        if not self.pk:
            super(School, self).save()
            self.relative_address = '/api/schools/' + str(self.pk)
        super(School, self).save()


class Course(BaseModel):
    SORT_CHOICES = [(1, 'Alone'), (2, 'With other'), (3, 'With 2 other')]
    school = models.ForeignKey('School', related_name='courses', on_delete=models.CASCADE, null=True, default=None)
    title = models.CharField(max_length=100)
    relative_address = models.CharField(max_length=256, null=True, blank=True)
    number_in_row = models.IntegerField(choices=SORT_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True, null=True)
    order_id = models.IntegerField(default=0, blank=False, null=False)
    lessons_count = models.IntegerField(default=0, blank=False, null=True)
    icon = models.ImageField(upload_to=course_icon_directory, null=True)

    class Meta(object):
        ordering = ('order_id',)

    def __str__(self):
        return self.title

    def save(self):
        if not self.pk:
            super(Course, self).save()
            self.relative_address = '/api/courses/' + str(self.pk)
            if self.icon:
                initial_path = self.icon.path
                filename = self.icon.name.split('None')
                self.icon.name = filename[0] + str(self.pk) + filename[1]
                new_path = settings.MEDIA_ROOT + '/' + self.icon.name
                os.rename(initial_path, new_path)
        super(Course, self).save()


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
            super(Lesson, self).save()
            self.relative_address = '/api/lessons/' + str(self.pk)
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
    image = models.ImageField(upload_to=parts_image, null=True, default=None, blank=True)
    order_id = models.IntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order_id',)

    def __str__(self):
        return self.title

    def save(self):
        if not self.pk:
            super(Part, self).save()
            if self.image:
                initial_path = self.image.path
                filename = self.image.name.split('None')
                self.image.name = filename[0] + str(self.pk) + filename[1]
                new_path = settings.MEDIA_ROOT + '/' + self.image.name
                os.rename(initial_path, new_path)
        super(Part, self).save()

