from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["size", "brand", "store", "shoe_type", "link", "price", "shoe_pic", "praise"]
