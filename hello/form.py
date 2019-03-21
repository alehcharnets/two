from django.forms import ModelForm
from . import models


class CommentsForm(ModelForm):
    class Meta():
        model = models.Comment
        fields = ["Comment_text"]
