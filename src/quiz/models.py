from django.db import models


class Exam(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'


class Question(models.Model):
    statement = models.TextField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='choices')
    score = models.IntegerField(default=1)
    hint = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.statement[:50]

    class Meta:
        ordering = ['id']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Choice(models.Model):
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['id']
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'