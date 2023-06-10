from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  price = models.PositiveIntegerField()
  description = models.TextField(blank=True)
  image = models.CharField(
      max_length=200, default='https://droider.ru/wp-content/uploads/2016/12/parcel-delivery-package.jpg')
  
  def __str__(self):
    return self.name

class Comment(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  userName = models.CharField(max_length=100)
  text = models.TextField()

  def __str__(self):
    return self.userName + ' ' + self.text[:25]

class Addresses(models.Model):
  city = models.CharField(max_length=50)
  street = models.CharField(max_length=50)
  house = models.CharField(max_length=10)

  def __str__(self):
    return self.city + ' ' + self.street + ' ' + self.house