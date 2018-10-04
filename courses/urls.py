from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('api/courses/', views.CourseApiView.as_view()),
    path('api/courses/<int:pk>', views.LessonApiView.as_view()),
    path('api/lessons/<int:pk>', views.PartApiView.as_view()),
    # path('api/parts/<int:pk>', views.PartApiView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
