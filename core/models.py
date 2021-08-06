from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField


# Create your models here.


def get_article_image_folder(instance, filename):
    return "%s/%s" % (instance.title, filename)


class Tag(models.Model):
    title = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    date_published = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(null=True, blank=True,
                             upload_to=get_article_image_folder)
    tags = models.ManyToManyField(Tag)
    views = models.IntegerField(default=0)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.title


class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
