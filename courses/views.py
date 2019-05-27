# from django.shortcuts import render
# from django.http import Http404
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SchoolSerializer, CourseSerializer, LessonSerializer, PartSerializer
from .models import School, Course, Lesson
from .utility import version_compare
import sys


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

def get_school(request):
    school_domain = request.META.get('HTTP_SCHOOL', None)
    if not school_domain:
        return None
    else:
        return School.get_or_fail_by_domain(school_domain)


def check_update(request):
    force_update = False
    norm_update = False
    update_app_address = None
    error_code = 0;
    print(str(request.META.get('HTTP_SCHOOL', None)), file=sys.stderr)
    print(str(request.META.get('HTTP_APP_VERSION', None)), file=sys.stderr)
    print(str(request.META.get('HTTP_APP_DEVICE', None)), file=sys.stderr)
    school_version = request.META.get('HTTP_APP_VERSION', None)
    school_app_device = request.META.get('HTTP_APP_DEVICE', None)
    school = get_school(request)
    if school and school_version and school_app_device:
        if version_compare(school.app_last_version, school_version) == 1:
            norm_update = True
            if version_compare(school.app_support_version, school_version) == 1:
                force_update = True
                error_code = 1
            if school_app_device == 'android':
                update_app_address = school.app_address
        return error_code, {"school_relative_address": school.relative_address,
                            "force_update": force_update,
                            "norm_update": norm_update,
                            "update_app_address": update_app_address,
                            "update_app_message": school.app_update_message}
    else:
        error_code = 2
        return error_code, None


class CourseApiView(APIView):
    def get(self, request, pk):
        error_code, data = check_update(request)
        if error_code == 1:
            return Response(data=data)
        elif error_code == 2:
            return HttpResponseBadRequest()
        school = School.objects.get(pk=pk)
        courses = school.courses.all()
        # serializer = CourseSerializer(Course.get_or_fail_by_pk(pk))
        serializer = CourseSerializer(courses, many=True)
        return Response(data=serializer.data)


class LessonApiView(APIView):
    def get(self, request, pk):
        error_code, data = check_update(request)
        if error_code == 1:
            return Response(data=data)
        elif error_code == 2:
            return HttpResponseBadRequest()
        course = Course.objects.get(pk=pk)
        lessons = course.lessons.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(data=serializer.data)


class PartApiView(APIView):
    def get(self, request, pk):
        error_code, data = check_update(request)
        if error_code == 1:
            return Response(data=data)
        elif error_code == 2:
            return HttpResponseBadRequest()
        lesson = Lesson.objects.get(pk=pk)
        parts = lesson.parts.all()
        serializer = PartSerializer(parts, many=True)
        return Response(data=serializer.data)


class AllSchoolsApiView(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(data=serializer.data)


class SchoolApiView(APIView):
    def get(self, request):
        _, data = check_update(request)
        return Response(data=data)