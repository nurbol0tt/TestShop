from django.db import models
from django.core.cache import cache


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        cache.delete('product_list')
        super().save(*args, **kwargs)
