from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    SIZE_CHOICES = (
        ('10.5', '10.5'),
        ('11', '11'),
        ('11.5', '11.5'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
    )
    size = models.CharField(max_length=4, choices=SIZE_CHOICES, verbose_name="Size (use US women's sizes)")
    brand = models.CharField(max_length=50)
    store = models.CharField(max_length=50)
    SHOE_TYPE_CHOICES = (
        ('ankle boots/booties', 'ankle boots/booties'),
        ('boots', 'boots'),
        ('flats', 'flats'),
        ('pumps/heels', 'pumps/heels'),
        ('sandals', 'sandals'),
        ('sneakers', 'sneakers'),
    )
    shoe_type = models.CharField(max_length=20, choices=SHOE_TYPE_CHOICES)
    link = models.CharField(max_length=200, blank=True, default="", verbose_name="link (optional)")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    praise = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    shoe_pic = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # outfit_photo

