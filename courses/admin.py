from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import School, Course, Lesson, Part


class CourseInLine(SortableInlineAdminMixin, admin.TabularInline):
    show_change_link = True
    model = Course
    readonly_fields = ('relative_address', 'created', 'icon_address')
    extra = 1


class LessonInLine(SortableInlineAdminMixin, admin.TabularInline):
    show_change_link = True
    model = Lesson
    extra = 1
    readonly_fields = ('school', 'relative_address',)
    # fields = ['title', 'course', 'school', 'order_id', 'relative_address']


class PartInLine(SortableInlineAdminMixin, admin.StackedInline):
    show_change_link = True
    model = Part
    extra = 0


@admin.register(School)
class SchoolAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'relative_address']
    readonly_fields = ('relative_address',)
    inlines = [CourseInLine]


@admin.register(Course)
class CourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'school', 'relative_address', 'created']
    readonly_fields = ('relative_address', 'icon_address')
    inlines = (LessonInLine,)


@admin.register(Lesson)
class LessonAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'school', 'course', 'relative_address']
    readonly_fields = ('relative_address', 'order_id')
    inlines = [PartInLine]


# admin.site.register(Category)


# @admin.register(Part)
# class PartAdmin(admin.ModelAdmin):
#     list_display = ['title']
