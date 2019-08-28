from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Clothes(models.Model):
    title = models.CharField(max_length=150)
    comment = models.TextField(blank=True)
    # image = CloudinaryField('image', blank=True, null=True,)
    image = models.ImageField(upload_to = 'clothes')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_purchase = models.DateField()

    def __str__(self):
        return self.title
