# from django.shortcuts import render
from django.http import HttpResponse
# from django.http import Http404
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.serializers import SchoolSerializer, CourseSerializer, LessonSerializer, PartSerializer
from .models import School, Course, Lesson


# @csrf_exempt
# def api_course(request):
#     courses = Course.objects.all()
#     courses_serialized = serializers.serialize('json', courses)
#     courses_json = json.loads(courses_serialized)
#     data = json.dumps(courses_json)
#     return HttpResponse(data)
#
#
# @csrf_exempt
# def api_lesson(request, id):
#     course = Course.objects.get(id=id)
#     lessons = course.lessons.all()
#     lessons_serialized = serializers.serialize('json', lessons)
#     lessons_json = json.loads(lessons_serialized)
#     data = json.dumps(lessons_json)
#     return HttpResponse(data)
#
#
# @csrf_exempt
# def api_part(request, id):
#     lesson = Lesson.objects.get(id=id)
#     parts = lesson.parts.all()
#     parts_serialized = serializers.serialize('json', parts)
#     parts_json = json.loads(parts_serialized)
#     data = json.dumps(parts_json)
#     return HttpResponse(data)


# class SchoolApiView(APIView):
#     def get(self, request, pk):
#         serializer = SchoolSerializer(School.objects.all(), many=True)
#         return Response(data=serializer.data)


class CourseApiView(APIView):
    def get(self, request, pk):
        school = School.objects.get(pk=pk)
        courses = school.courses.all()
        # serializer = CourseSerializer(Course.get_or_fail_by_pk(pk))
        serializer = CourseSerializer(courses, many=True)
        return Response(data=serializer.data)


class LessonApiView(APIView):
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        lessons = course.lessons.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(data=serializer.data)


class PartApiView(APIView):
    def get(self, request, pk):
        lesson = Lesson.objects.get(pk=pk)
        parts = lesson.parts.all()
        serializer = PartSerializer(parts, many=True)
        return Response(data=serializer.data)


class AllSchoolsApiView(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(data=serializer.data)


# class SchoolsApiView(APIView):
# def get(self, request, pk):
    #     serializer = SchoolSerializer(School.get_or_fail_by_pk(pk))
    #     return Response(data=serializer.data)