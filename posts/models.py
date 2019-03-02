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
    MENS_WOMENS_CHOICE = (
        ("mens", "mens"),
        ("womens", "womens"),
    )
    mens_or_womens = models.CharField(max_length=6, choices=MENS_WOMENS_CHOICE, verbose_name="Men's or Women's Shoe Section", default='womens')
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
    PURCHASED_CHOICES = (
        ('online', 'online'),
        ('in-store', 'in-store'),
    )
    purchased = models.CharField(max_length=9, choices=PURCHASED_CHOICES, verbose_name="Purchased Online or In-Store")
    praise = models.TextField(verbose_name="Praise/Comments/More Information")
    date = models.DateTimeField(auto_now_add=True)
    shoe_pic = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # outfit_photo

