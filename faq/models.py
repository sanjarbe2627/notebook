from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
