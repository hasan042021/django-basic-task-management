from django.db import models
from categories import models as catModel


# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)
    assignDate = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(catModel.Categories)

    def __str__(self):
        return f"{self.title} "
