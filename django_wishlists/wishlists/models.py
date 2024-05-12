from django.db import models

from users.models import User


class Item(models.Model):
    """
    Model for an item that a user wants to add to their wishlist.
    """
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    product_url = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Wishlist(models.Model):
    """
    Model for a user's wishlist. Can contain multiple items.
    """
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f'name: {self.name}, items:{self.items}'
