from django.db import models
# from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class Video(models.Model):
    class Meta():
        db_table = "Video"
        # ordering = ['-Video_data']

    Video_url = models.URLField()
    Video_name = models.CharField(max_length=200)
    Video_description = models.TextField()
    Video_data = models.DateTimeField(auto_now_add=True)
    # Video_data = models.DateTimeField(default = datetime.now, blank = True)
    Video_likes = models.IntegerField(default=0)
    Video_dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.Video_name

    def get_absolute_url(self):
        return reverse('one_video_url', args=[self.id])


class Comment(models.Model):
    class Meta():
        db_table = "Comment"
        ordering = ['-Comment_data']

    Comment_text = models.TextField(verbose_name="New comment")
    Comment_data = models.DateTimeField(auto_now_add=True)
    # Comment_data = models.DateTimeField(default=datetime.now, blank=True)
    Comment_Video = models.ForeignKey(Video, on_delete=models.CASCADE)
    Comment_User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Comment_text

# Create your models here.
