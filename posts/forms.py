from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["size", "brand", "store",  "mens_or_womens", "shoe_type", "link", "price", "purchased", "shoe_pic", "praise"]
