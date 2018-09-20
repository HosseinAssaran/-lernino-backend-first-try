from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('api/courses/', views.CourseApiView.as_view()),
    path('api/courses/<int:pk>', views.SingleCourseApiView.as_view()),
    path('api/<int:order_id>/lessons/', views.LessonApiView.as_view()),
    path('api/<int:order_id>/parts/', views.PartApiView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
