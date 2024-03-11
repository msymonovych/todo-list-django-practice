from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    def __str__(self):
        return self.content
