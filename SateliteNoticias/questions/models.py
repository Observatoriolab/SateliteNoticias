from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.
class Question(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=240)
    content = models.TextField(blank=True)
    # Pseudo ID to retrieve the details of a single question
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="questions")
    tags = TaggableManager(blank = True) 

    def __str__(self):
        return self.title

class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    question = models.ForeignKey(Question,
                                on_delete=models.CASCADE,
                                related_name="answers")

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="votes")

    tags = TaggableManager(blank = True) 

    def __str__(self):
        return self.author.username

