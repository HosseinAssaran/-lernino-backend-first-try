from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import Course, Lesson, Part
# from categories import Category


class LessonInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = Lesson
    readonly_fields = ('relative_address',)


class PartInLine(SortableInlineAdminMixin, admin.StackedInline):
    model = Part
    extra = 0


@admin.register(Course)
class CourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'order_id', 'relative_address', 'created']
    readonly_fields = ('relative_address', 'icon_address')
    inlines = [LessonInLine]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order_id', 'relative_address']
    readonly_fields = ('relative_address',)
    inlines = [PartInLine]


# admin.site.register(Category)


# @admin.register(Part)
# class PartAdmin(admin.ModelAdmin):
#     list_display = ['title']
