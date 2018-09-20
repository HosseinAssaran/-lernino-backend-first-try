# from django.shortcuts import render
from django.http import HttpResponse
# from django.http import Http404
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.serializers import CourseSerializer, LessonSerializer, PartSerializer
from .models import Course, Lesson


@csrf_exempt
def api_course(request):
    courses = Course.objects.all()
    courses_serialized = serializers.serialize('json', courses)
    courses_json = json.loads(courses_serialized)
    data = json.dumps(courses_json)
    return HttpResponse(data)


@csrf_exempt
def api_lesson(request, id):
    course = Course.objects.get(id=id)
    lessons = course.lessons.all()
    lessons_serialized = serializers.serialize('json', lessons)
    lessons_json = json.loads(lessons_serialized)
    data = json.dumps(lessons_json)
    return HttpResponse(data)


@csrf_exempt
def api_part(request, id):
    lesson = Lesson.objects.get(id=id)
    parts = lesson.parts.all()
    parts_serialized = serializers.serialize('json', parts)
    parts_json = json.loads(parts_serialized)
    data = json.dumps(parts_json)
    return HttpResponse(data)


class CourseApiView(APIView):
    def get(self, request):
        serializer = CourseSerializer(Course.objects.all(), many=True)
        return Response(data=serializer.data)


class SingleCourseApiView(APIView):
    def get(self, request, pk):
        serializer = CourseSerializer(Course.get_or_fail_by_pk(pk))
        return Response(data=serializer.data)


class LessonApiView(APIView):
    def get(self, request, order_id):
        course = Course.objects.get(order_id=order_id)
        lessons = course.lessons.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(data=serializer.data)


class PartApiView(APIView):
    def get(self, request, order_id):
        lesson = Lesson.objects.get(order_id=order_id)
        parts = lesson.parts.all()
        serializer = PartSerializer(parts, many=True)
        return Response(data=serializer.data)