from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('api/schools/<int:pk>', views.CourseApiView.as_view()),
    path('api/courses/<int:pk>', views.LessonApiView.as_view()),
    path('api/lessons/<int:pk>', views.PartApiView.as_view()),
    path('api/schools', views.AllSchoolsApiView.as_view()),
    path('api/school_info', views.SchoolApiView.as_view()),
    # path('api/parts/<int:pk>', views.PartApiView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
