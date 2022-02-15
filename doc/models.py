from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import uuid

# Create your models here.


class Topic(models.Model):
    NUM_CHOICE = (
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9'),
        ('ten', '10')
    )
    owner = models.ForeignKey(
        User, null=True, blank=True, on_delete=CASCADE)
    topic = models.CharField(max_length=200)
    page_no = models.CharField(unique=True, max_length=100, choices=NUM_CHOICE)

    # @filename: topic name, ex> linux
    filename = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.topic)

    class Meta:
        ordering = ['created']


class Note(models.Model):
    COLOR_TYPE = (
        ('#d783ff', 'light purple'),
        ('#6f42c1', 'purple'),
        ('#e83e8c', 'pink'),
        ('#dc6c5f', 'orange'),
        ('#64b9d2', 'light-blue'),
    )

    title = models.CharField(max_length=200)
    belong_to = models.ForeignKey(
        Topic, null=True, blank=True, on_delete=CASCADE)
    color = models.CharField(max_length=100, choices=COLOR_TYPE)
    intro = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=0, null=True, blank=True)

    # @filename: note name, ex> bash
    filename = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['created']

    @property
    def total(self):
        no = Note.objects.all.count()
        if no == None:
            return 1
        else:
            return no + 1
