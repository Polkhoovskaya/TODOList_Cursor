from django.db import models


class Todo(models.Model):
    """Single todo item with optional description and due date."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['is_completed', 'due_date', 'title']

    def __str__(self) -> str:
        status = '✅' if self.is_completed else '⬜'
        return f'{status} {self.title}'
