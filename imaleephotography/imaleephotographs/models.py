from django.db import models
from django.urls import reverse


# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=250,unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.name

class Messages(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
        return reverse('imaleephotographs:image_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Image(models.Model):
    name = models.CharField(max_length=250, unique=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    def get_url(self):
        return reverse('imaleephotographs:ImgCatDetails',args=[self.Category.slug,self.slug])
    def __str__(self):
        return '{}'.format(self.name)