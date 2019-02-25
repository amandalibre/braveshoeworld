from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    shoe_name = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=25)
    brand = models.CharField(max_length=50)
    store = models.CharField(max_length=50)
    link = models.CharField(max_length=200, blank=True, default="")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    slug = models.SlugField()
    praise = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    shoe_pic = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # outfit_photo

    def __str__(self):
        return self.shoe_name

