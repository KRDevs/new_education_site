from django.contrib import admin
from .models import Subject, Lesson, Author, Test, TestOption, TestPractice, TestOptionPractice, Practice

admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Practice)
admin.site.register(Author)
admin.site.register(Test)
admin.site.register(TestPractice)
admin.site.register(TestOptionPractice)
admin.site.register(TestOption)
