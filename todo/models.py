from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
  dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  dateModified = models.DateTimeField(null=True, blank=True, default=timezone.now)
  createdBy = models.CharField(max_length=1000, null=True, blank=True)
  modifiedBy = models.CharField(max_length=1000, null=True, blank=True)
  bookID = models.FloatField(null=True,blank=True,default=0)
  title = models.CharField(max_length=500)
  authors = models.CharField(max_length=500)
  rating = models.CharField(max_length=500)
  isbn = models.CharField(max_length=500)
  languageCode = models.CharField(max_length=500)
  ratingCount = models.CharField(max_length=1000, null=True, blank=True)
  price = models.CharField(max_length=1000, null=True, blank=True)
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False,blank=False)
    created_at = models.DateTimeField(default=timezone.now)

class CartItem(models.Model):
    product = models.ForeignKey(Todo, on_delete=models.CASCADE,null=False,blank=False)
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=False,blank=False)

    TAX_AMOUNT = 19.25

    def price_ttc(self):
        return self.price_ht * (1 + TAX_AMOUNT/100.0)

    def __str__(self):
        return  self.price_ht + " - " + self.product