from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


app_name='Tech'

urlpatterns = [
    path('<int:course_id>/', views.detail, name='detail'),
    path('', views.courses, name='home-page'),
    path('<int:course_id>/yourchoice/', views.yourchoice, name='yourchoice'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)