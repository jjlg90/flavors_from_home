from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.db.models import Avg


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    upc = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    brand = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_avg_rating(self):
        try:
            rating = Reviews.objects.filter(product=self.pk).aggregate(Avg('user_rating'))
            rating = rating['user_rating__avg']
        except:
            rating = 0
        return rating


class Reviews(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'

    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254, null=False, blank=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='reviews')
    user_rating = models.DecimalField(
        default=1,
        max_digits=3,
        decimal_places=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    created = models.DateTimeField(default=timezone.now, editable=False)
    comment = models.TextField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Reviews, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_product(self):
        return self.product

    def get_name(self):
        if self.user_profile:
            return self.user_profile.user.get_full_name()
        return None
