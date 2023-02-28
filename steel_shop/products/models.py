from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


User = get_user_model()


class Category(models.Model):
    name_cat = models.CharField('Название подкатегории', max_length=250)
    slug =  models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
       return reverse('products:', kwargs={'id': self.id, 'name': self.name})

    



class Subcategory(models.Model):
    name = models.CharField('Название подкатегории', max_length=250)
    slug = models.SlugField(max_length=50, unique=True)
    categories = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)


class Product(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
        )
    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )

    def __str__(self):
        return self.text[:50]

    class Meta:
        ordering = ['-pub_date']