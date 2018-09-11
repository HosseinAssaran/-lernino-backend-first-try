from django.contrib import admin

from .models import Course, Lesson, Part


class LessonInLine(admin.StackedInline):
    model = Lesson


class PartInLine(admin.StackedInline):
    model = Part


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']
    readonly_fields = ('relative_address',)
    inlines = [LessonInLine]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    readonly_fields = ('relative_address',)
    inlines = [PartInLine]


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['title']
