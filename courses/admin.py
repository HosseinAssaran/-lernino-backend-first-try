from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import School, Course, Lesson, Part


class CourseInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = Course
    show_change_link = True
    readonly_fields = ('relative_address', 'created',)
    extra = 1


class LessonInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ['title', 'school', 'order_id', 'relative_address']
    show_change_link = True
    readonly_fields = ('school', 'relative_address', 'course',)


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
    list_display = ['title', 'school', 'order_id', 'relative_address', 'created']
    readonly_fields = ('relative_address', 'icon_address')
    inlines = (LessonInLine,)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'school', 'course', 'order_id', 'relative_address']
    readonly_fields = ('relative_address',)
    inlines = [PartInLine]


# admin.site.register(Category)


# @admin.register(Part)
# class PartAdmin(admin.ModelAdmin):
#     list_display = ['title']
