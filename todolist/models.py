from django.db import models


# COLLECTION MODEL
class Collection(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.title