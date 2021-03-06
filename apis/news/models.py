from django.db import models
from apis.accounts.models import User

# Create your models here.


class News(models.Model):
    CATEGORY = (("0", "Politics",), ("1", "Sports"),
                ("2", "Fashion"), ("3", "Technology"))
    title = models.CharField(max_length=255)
    story = models.TextField()
    category = models.CharField(choices=CATEGORY, max_length=2)
    reporter = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="news")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
