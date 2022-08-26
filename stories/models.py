from users.models import ProfileModel
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')
    last_accessed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(blank=True, null=True, max_length=100)


    authors = models.ManyToManyField('Author', blank=True)
    writer = models.CharField(blank=True, null=True, max_length=30)

    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)

    about =  models.ManyToManyField(ProfileModel, blank=True)
    about_who =  models.CharField(max_length=30, blank=True, null=True)

    story = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
