from django.contrib import admin

from .models import Course, Lesson, Part
# from categories import Category


class LessonInLine(admin.TabularInline):
    model = Lesson
    readonly_fields = ('relative_address',)


class PartInLine(admin.StackedInline):
    model = Part
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'order_id', 'created']
    readonly_fields = ('relative_address', 'icon_address')
    inlines = [LessonInLine]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'order_id']
    readonly_fields = ('relative_address',)
    inlines = [PartInLine]


# admin.site.register(Category)


# @admin.register(Part)
# class PartAdmin(admin.ModelAdmin):
#     list_display = ['title']
