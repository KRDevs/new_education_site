from django.urls import path

from subject.views import subject_list, subject_detail, practice_detail, lesson_detail, lesson_list, video_stream, \
    practice_video_stream

urlpatterns = [
    path('', subject_list, name='subject_list'),
    path('subject/<int:pk>/', subject_detail, name='subject_detail'),
    path('lessons/', lesson_list, name='lesson_list'),
    path('lesson/<int:pk>/', lesson_detail, name='lesson_detail'),
    path('practice/<int:pk>/', practice_detail, name='practice_detail'),
    path('lesson/<int:pk>/video/', video_stream, name='video_stream'),
    path('practice/<int:pk>/video_practice/', practice_video_stream, name='practice_video_stream'),
]
