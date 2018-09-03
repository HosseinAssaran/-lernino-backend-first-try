from django.contrib import admin

from .models import Course, Lesson, Page


class LessonInLine(admin.StackedInline):
    model = Lesson

class PageInLine(admin.StackedInline):
    model = Page

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [LessonInLine]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [PageInLine]

@admin.register(Page)
class FlashCardAdmin(admin.ModelAdmin):
    list_display = ['key']