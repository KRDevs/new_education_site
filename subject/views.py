import os

from django.http import HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404

from core import settings
from .models import Subject, Lesson, Test, Practice, TestPractice


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})


def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    lessons = Lesson.objects.filter(subject=subject)
    practices = Practice.objects.filter(subject=subject)
    return render(request, 'subject_detail.html', {'subject': subject, 'lessons': lessons, 'practices': practices})


def lesson_list(request):
    lessons = Lesson.objects.all()
    practices = Practice.objects.all()
    return render(request, 'lesson_list.html',
                  {'lessons': lessons,
                   'practices': practices})


def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    tests = Test.objects.filter(lesson=lesson).prefetch_related("options")

    return render(request, 'lesson_detail.html', {'lesson': lesson, 'tests': tests})


def practice_detail(request, pk):
    practice = get_object_or_404(Practice, pk=pk)
    tests = TestPractice.objects.filter(practice=practice).prefetch_related("practice_options")

    return render(request, 'practice_detail.html', {'practice': practice, 'tests': tests})


def video_stream(request, pk):  # `filename` o‘rniga `pk`
    lesson = get_object_or_404(Lesson, pk=pk)

    if not lesson.video:
        return HttpResponse("Video mavjud emas", status=404)

    file_path = os.path.join(settings.MEDIA_ROOT, str(lesson.video))

    if not os.path.exists(file_path):
        return HttpResponse("Fayl topilmadi", status=404)

    response = FileResponse(open(file_path, 'rb'), content_type='video/mp4')
    response['Accept-Ranges'] = 'bytes'  # 🔥 Video seek ishlashi uchun

    return response


def practice_video_stream(request, pk):  # `filename` o‘rniga `pk`
    practice = get_object_or_404(Practice, pk=pk)

    if not practice.video_practice:
        return HttpResponse("Video mavjud emas", status=404)

    file_path = os.path.join(settings.MEDIA_ROOT, str(practice.video_practice))

    if not os.path.exists(file_path):
        return HttpResponse("Fayl topilmadi", status=404)

    response = FileResponse(open(file_path, 'rb'), content_type='video/mp4')
    response['Accept-Ranges'] = 'bytes'  # 🔥 Video seek ishlashi uchun

    return response
