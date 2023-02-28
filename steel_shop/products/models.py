from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


User = get_user_model()


class Category(models.Model):
    name_cat = models.CharField('Название подкатегории', max_length=250)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('products:products_category',  args=[self.slug])


class Subcategory(models.Model):
    name = models.CharField('Название подкатегории', max_length=250)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey(
        Category, 
        verbose_name='Подкатегория', 
        on_delete=models.SET_NULL,
        related_name='subcategories'
        )

    def get_absolute_url(self):
        return reverse('products:products_subcategory',
                       kwargs={'cat_slug': self.category.slug,
                               'subcat_slug': self.slug}
                       )    


class Product(models.Model):
    base_price = models.IntegerField('Базовая цена')
    coeff_tonne_metre = models.IntegerField('Коэфф. пересчета тонны в метры')
    coeff_dicscount = models.DecimalField('Коэфф. скидки',
                                          max_digits=3,  decimal_places=2)
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