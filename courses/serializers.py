from rest_framework import serializers

from courses.models import Course, Lesson, Part


class PartSerializer(serializers.ModelSerializer):
    key = serializers.SerializerMethodField('get_id')

    class Meta:
        model = Part
        fields = '__all__'

    def get_id(self, obj):
        return str(obj.id)


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'relative_address', 'icon', 'number_in_row')

