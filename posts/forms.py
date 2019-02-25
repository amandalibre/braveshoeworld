from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["shoe_name", "size", "color", "brand", "store", "link", "price", "slug", "praise", "shoe_pic"]
