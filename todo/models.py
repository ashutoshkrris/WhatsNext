from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title