from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"


class Subject(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    calendar_plan = models.FileField(upload_to="uploads/kalendar_reja/", blank=True, null=True)
    outline = models.FileField(upload_to="uploads/mundarija/", blank=True, null=True)
    author = models.ManyToManyField(Author, related_name='subjects')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Fan'
        verbose_name_plural = 'Fanlar'


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, related_name="subject", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to="uploads/videolar/", blank=True, verbose_name="Asosiy mavzu videosi")
    presentation = models.FileField(upload_to="uploads/presentations/", blank=True, verbose_name="Taqdimot")
    lesson_plan = models.FileField(upload_to="uploads/dars_ishlanmalar/", blank=True, verbose_name="Dars ishlanmalar")
    word_theme = models.FileField(upload_to="uploads/word_mavzular/", blank=True, verbose_name="Word mavzular")
    questions = models.FileField(upload_to="uploads/nazorat_savollar/", blank=True, verbose_name="Nazorat savollar")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Dars'
        verbose_name_plural = 'Darslar'


class Practice(models.Model):
    subject = models.ForeignKey(Subject, related_name="subject_practice", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    video_practice = models.FileField(upload_to="uploads/videolar/", blank=True, verbose_name="Amaliyot videosi")
    presentation_practice = models.FileField(upload_to="uploads/presentations/", blank=True,
                                             verbose_name="Amaliyot taqdimoti")
    lesson_plan_practice = models.FileField(upload_to="uploads/dars_ishlanmalar/", blank=True,
                                            verbose_name="Dars ishlanmalar amaliyot")
    word_theme_practice = models.FileField(upload_to="uploads/word_mavzular/", blank=True,
                                           verbose_name="Word mavzular amaliyot")
    questions_practice = models.FileField(upload_to="uploads/nazorat_savollar/", blank=True,
                                          verbose_name="Nazorat savollar amaliyot")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Amaliyot'
        verbose_name_plural = 'Amaliyotlar'


class Test(models.Model):
    lesson = models.ForeignKey(Lesson, related_name="tests", on_delete=models.CASCADE)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Test'
        verbose_name_plural = 'Testlar'


class TestOption(models.Model):
    test = models.ForeignKey(Test, related_name="options", on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Variant'
        verbose_name_plural = 'Variantlar'


class TestPractice(models.Model):
    practice = models.ForeignKey(Practice, related_name="tests", on_delete=models.CASCADE)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Amaliyot Testi'
        verbose_name_plural = 'Amaliyot Testlari'


class TestOptionPractice(models.Model):
    test = models.ForeignKey(TestPractice, related_name="practice_options", on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Amaliyot Testi Varianti'
        verbose_name_plural = 'Amaliyot Testi Variantlari'
