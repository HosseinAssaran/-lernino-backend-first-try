from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import School, Course, Lesson, Part
from django import forms


class CourseInLine(SortableInlineAdminMixin, admin.TabularInline):
    show_change_link = True
    model = Course
    readonly_fields = ('relative_address', 'created',)
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


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        app_last_version = cleaned_data.get("app_last_version")
        app_address = cleaned_data.get("app_address")

        if app_last_version and not app_address:
            msg = "Must be filled if app last version filled."
            self.add_error('app_address', msg)


@admin.register(School)
class SchoolAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = SchoolForm
    list_display = ['title', 'relative_address']
    readonly_fields = ('relative_address',)
    inlines = [CourseInLine]


@admin.register(Course)
class CourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'school', 'lessons_count', 'relative_address', 'created']
    readonly_fields = ('relative_address', )
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
