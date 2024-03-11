from django.test import TestCase
from django.urls import reverse

from todo.models import Task, Tag


class TaskTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            name="test"
        )
        Tag.objects.create(
            name="test 2"
        )
        Task.objects.create(
            content="test content 1",
        ).tags.add(self.tag)

        Task.objects.create(
            content="test content 2",
        ).tags.add(self.tag)

    def test_retrieve_tasks(self):
        response = self.client.get(
            reverse("todo:task-list")
        )
        tasks = Task.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )
        self.assertTemplateUsed(response, "todo/task_list.html")

    def test_retrieve_tags(self):
        response = self.client.get(
            reverse("todo:tag-list")
        )
        tags = Tag.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["tag_list"]),
            list(tags)
        )
        self.assertTemplateUsed(response, "todo/tag_list.html")
