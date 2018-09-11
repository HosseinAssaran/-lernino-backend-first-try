from django.urls import path

from . import views

urlpatterns = [
    path('api/courses/', views.CourseApiView.as_view()),
    path('api/courses/<int:pk>', views.SingleCourseApiView.as_view()),
    path('api/<int:pk>/lessons/', views.LessonApiView.as_view()),
    path('api/<int:pk>/parts/', views.PartApiView.as_view()),

]
